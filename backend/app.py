import cv2
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from ultralytics import YOLO
import os
import uuid
import time
import threading
import pathlib
import sys

# -------------------------------
# CONFIGURATION & SETUP
# -------------------------------
base_dir = pathlib.Path(__file__).parent
UPLOAD_FOLDER = base_dir / "uploads"
FRAMES_FOLDER = base_dir / "output_frames"
MODEL_PATH = base_dir / "model/best.pt"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(FRAMES_FOLDER, exist_ok=True)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/output_frames", StaticFiles(directory=FRAMES_FOLDER), name="output_frames")

# Load Model
try:
    print(f"Loading model from {MODEL_PATH}...", flush=True)
    model = YOLO(str(MODEL_PATH))
    print("Model loaded successfully.", flush=True)
except Exception as e:
    print(f"Error loading model: {e}", flush=True)

# -------------------------------
# GLOBAL STATE
# -------------------------------
# We use a simple global lock to ensure we don't open multiple 
# camera streams simultaneously on the same hardware.
camera_lock = threading.Lock()
stop_event = threading.Event()

# -------------------------------
# UTILITY ENDPOINTS
# -------------------------------

@app.get("/health")
def health_check():
    return {"status": "ok"}

# -------------------------------
# IMAGE / VIDEO DETECTION
# -------------------------------

@app.post("/detect-image/")
async def detect_image(file: UploadFile = File(...)):
    file_ext = os.path.splitext(file.filename)[-1].lower()
    file_id = f"{uuid.uuid4()}{file_ext}"
    input_path = UPLOAD_FOLDER / file_id

    with open(input_path, "wb") as f:
        f.write(await file.read())

    results = model(str(input_path))
    output_filename = f"out_{file_id}"
    output_path = UPLOAD_FOLDER / output_filename
    
    for result in results:
        cv2.imwrite(str(output_path), result.plot())
        break 

    from fastapi.responses import FileResponse
    return FileResponse(output_path, media_type="image/jpeg")


@app.post("/detect-video/")
async def detect_video(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    file_ext = os.path.splitext(file.filename)[-1]
    video_filename = f"{file_id}{file_ext}"
    video_path = UPLOAD_FOLDER / video_filename

    with open(video_path, "wb") as f:
        f.write(await file.read())

    frame_output_dir = FRAMES_FOLDER / file_id
    os.makedirs(frame_output_dir, exist_ok=True)

    cap = cv2.VideoCapture(str(video_path))
    frame_skip = 5          
    frame_count = 0
    saved_frames = 0
    max_frames = 20         
    image_urls = []

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame_count += 1
            if frame_count % frame_skip != 0:
                continue

            results = model(frame, verbose=False)
            if len(results[0].boxes) > 0:
                img_name = f"{file_id}_{frame_count}.jpg"
                save_path = frame_output_dir / img_name
                cv2.imwrite(str(save_path), results[0].plot())
                saved_frames += 1
                image_urls.append(f"http://127.0.0.1:8000/output_frames/{file_id}/{img_name}")

            if saved_frames >= max_frames:
                break
    finally:
        cap.release()

    if not image_urls:
        return {"message": "No detections found", "images": []}
    return {"images": image_urls}


# -------------------------------
# ROBUST LIVE STREAMING
# -------------------------------

@app.post("/stop-live/")
def stop_live():
    # Signal the loop to stop
    print("Stop signal received...", flush=True)
    stop_event.set()
    return {"message": "Stopping..."}

@app.get("/live-detect/")
def live_detect(camera_id: int = 1):
    # Only allow one client to initialize the camera stream at a time
    # to prevent hardware conflicts.
    
    def frame_generator():
        # Acquire lock to ensure we own the camera hardware
        locked = camera_lock.acquire(blocking=False)
        if not locked:
             print("Camera is busy. Attempting to force release via stop event...", flush=True)
             stop_event.set()
             time.sleep(1) # Give existing thread time to exit
             # Try acquiring again
             locked = camera_lock.acquire(blocking=False)
             if not locked:
                 print("Could not acquire camera lock.", flush=True)
                 return
        
        stop_event.clear()
        
        print(f"Opening Camera {camera_id}...", flush=True)
        # Use DirectShow on Windows for better compatibility
        cap = cv2.VideoCapture(camera_id, cv2.CAP_DSHOW)
        
        # Verify camera is actually working by reading one frame
        if cap.isOpened():
             ret, _ = cap.read()
             if not ret:
                 print(f"Camera {camera_id} opened but returned no frame.", flush=True)
                 cap.release()
        
        if not cap.isOpened():
            print("Trying Camera 0...", flush=True)
            cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


            
        if not cap.isOpened():
             print("Failed to open any camera.", flush=True)
             camera_lock.release()
             return

        # Optimize Camera
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        cap.set(cv2.CAP_PROP_FPS, 30)

        frame_idx = 0
        last_annotated_frame = None
        
        print("Starting stream loop...", flush=True)
        
        try:
            while not stop_event.is_set():
                ret, frame = cap.read()
                if not ret:
                    print("Camera read failed.", flush=True)
                    break

                frame_idx += 1
                
                # Resize for performance (consistent 480x360)
                frame_small = cv2.resize(frame, (480, 360))
                
                # Run YOLO every 5 frames
                should_run_yolo = (frame_idx % 5 == 0)
                
                if should_run_yolo:
                    try:
                        # Fast inference
                        results = model.predict(frame_small, verbose=False, conf=0.3, imgsz=320)
                        last_annotated_frame = results[0].plot()
                    except Exception as e:
                        print(f"YOLO Error: {e}", flush=True)
                        last_annotated_frame = frame_small # Fallback
                
                # DECISION: What to yield?
                # Option A: Smooth video (raw frame) + flickering boxes (if overlaying)
                # Option B: Stuttery video (repeat last annotated frame) - Guarantees 'detection view'
                # Option C: Raw video most of the time, annotated frame when ready. 
                # The user suggested: "If YOLO skipped, send last known annotated frame or normal frame"
                # Let's yield the last_annotated_frame if we have it, to persist the boxes. 
                # This makes the video FPS effective = YOLO FPS (low). 
                # BUT, to prevent total freeze, we yield *something* every loop.
                
                if last_annotated_frame is None:
                    output_frame = frame_small
                else:
                    output_frame = last_annotated_frame

                # Timestamp
                cv2.putText(output_frame, f"Live: {time.ctime()} | Frame {frame_idx}", (10, 20), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

                success, jpeg = cv2.imencode('.jpg', output_frame)
                if not success:
                    continue
                
                yield (
                    b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n\r\n" + jpeg.tobytes() + b"\r\n"
                )
                
                # Small sleep to yield CPU if needed, though CV2 usually blocks enough
                # time.sleep(0.01)

        except Exception as e:
            print(f"Stream Loop Exception: {e}", flush=True)
        finally:
            print("Releasing camera...", flush=True)
            cap.release()
            camera_lock.release()
            print("Camera released and lock freed.", flush=True)

    return StreamingResponse(
        frame_generator(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )
