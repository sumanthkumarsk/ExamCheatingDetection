# from fastapi import FastAPI, File, UploadFile
# from fastapi.responses import FileResponse
# from fastapi.middleware.cors import CORSMiddleware
# from ultralytics import YOLO
# import os
# import uuid

# app = FastAPI()

# # Allow frontend requests
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # you can specify ["http://localhost:5173"]
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load YOLOv8 model (✅ correct way)
# model_path = "model/best.pt"
# model = YOLO(model_path)

# UPLOAD_FOLDER = "uploads"
# RESULT_FOLDER = "runs/detect"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(RESULT_FOLDER, exist_ok=True)

# # @app.post("/detect/")
# async def detect(file: UploadFile = File(...)):
#     file_ext = os.path.splitext(file.filename)[1]
#     file_id = str(uuid.uuid4()) + file_ext
#     input_path = os.path.join(UPLOAD_FOLDER, file_id)

#     # Save uploaded file
#     with open(input_path, "wb") as f:
#         f.write(await file.read())

#     # Run YOLOv8 detection (✅ correct method)
#     results = model.predict(source=input_path, save=True, project=RESULT_FOLDER, name=file_id)

#     # Get the path of the saved file (YOLO saves inside RESULT_FOLDER/name)
#     saved_dir = os.path.join(RESULT_FOLDER, file_id)
#     saved_files = os.listdir(saved_dir)
#     if not saved_files:
#         return {"error": "No output generated"}
#     saved_path = os.path.join(saved_dir, saved_files[0])

#     return FileResponse(saved_path)

# @app.post("/detect/")
# async def detect(file: UploadFile = File(...)):
#     file_ext = os.path.splitext(file.filename)[-1].lower()

#     file_id = str(uuid.uuid4())
#     input_filename = f"{file_id}{file_ext}"
#     input_path = os.path.join(UPLOAD_FOLDER, input_filename)

#     # Save uploaded file
#     with open(input_path, "wb") as f:
#         f.write(await file.read())

#     # Run YOLOv8 on image OR video
#     results = model.predict(
#         source=input_path, 
#         save=True,
#         save_txt=False,
#     save_conf=False, 
#         project=RESULT_FOLDER, 
#         name=file_id,
#         vid_stride=1  # important for video
#     )

#     # YOLO saves output in /runs/detect/{file_id}/
#     output_dir = os.path.join(RESULT_FOLDER, file_id)
#     output_files = os.listdir(output_dir)

#     if not output_files:
#         return {"error": "No output generated"}

#     output_file = output_files[0]  # image OR video
#     output_path = os.path.join(output_dir, output_file)

#     # return correct content-type
#     media_type = (
#         "video/mp4" if output_file.endswith(".mp4") else "image/jpeg"
#     )

#     return FileResponse(output_path, media_type=media_type)




# 3




# from fastapi import FastAPI, File, UploadFile
# from fastapi.responses import FileResponse
# from fastapi.middleware.cors import CORSMiddleware
# from ultralytics import YOLO
# import os
# import uuid

# app = FastAPI()

# # Allow frontend
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Paths
# UPLOAD_FOLDER = "uploads"
# RESULT_FOLDER = "runs/detect"

# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(RESULT_FOLDER, exist_ok=True)

# # Load YOLO model
# model = YOLO("model/best.pt")

# @app.post("/detect/")
# async def detect(file: UploadFile = File(...)):
#     file_ext = os.path.splitext(file.filename)[-1].lower()
#     file_id = str(uuid.uuid4())
#     input_path = os.path.join(UPLOAD_FOLDER, f"{file_id}{file_ext}")

#     # Save file
#     with open(input_path, "wb") as f:
#         f.write(await file.read())

#     # Run YOLO (video OR image)
#     results = model.predict(
#         source=input_path,
#         save=True,
#         save_txt=False,
#         save_conf=False,
#         vid_stride=1,
#         project=RESULT_FOLDER,
#         name=file_id
#     )

#     # Output folder
#     output_dir = os.path.join(RESULT_FOLDER, file_id)
#     output_files = os.listdir(output_dir)

#     if not output_files:
#         return {"error": "No output generated"}

#     # Priority: return video if exists
#     video_files = [
#         f for f in output_files
#         if f.endswith((".mp4", ".avi", ".mov"))
#     ]

#     if video_files:
#         video_path = os.path.join(output_dir, video_files[0])
#         return FileResponse(video_path, media_type="video/mp4")

#     # Otherwise return first image
#     image_files = [
#         f for f in output_files 
#         if f.endswith((".jpg", ".jpeg", ".png"))
#     ]

#     if image_files:
#         image_path = os.path.join(output_dir, image_files[0])
#         return FileResponse(image_path, media_type="image/jpeg")

#     return {"error": "Output file not recognized"}



# import cv2
# import zipfile
# import shutil
# from fastapi import FastAPI, UploadFile, File
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import FileResponse
# from ultralytics import YOLO
# import os
# import uuid

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# model = YOLO("model/best.pt")

# UPLOAD_FOLDER = "uploads"
# FRAMES_FOLDER = "output_frames"
# ZIP_FOLDER = "zip_output"

# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(FRAMES_FOLDER, exist_ok=True)
# os.makedirs(ZIP_FOLDER, exist_ok=True)

# @app.post("/detect-video/")
# async def detect_video(file: UploadFile = File(...)):
#     # unique ID for request
#     file_id = str(uuid.uuid4())

#     # Save input video
#     file_ext = os.path.splitext(file.filename)[-1]
#     video_path = os.path.join(UPLOAD_FOLDER, f"{file_id}{file_ext}")

#     with open(video_path, "wb") as f:
#         f.write(await file.read())

#     # Folder to save detection frames
#     frame_output_dir = os.path.join(FRAMES_FOLDER, file_id)
#     os.makedirs(frame_output_dir, exist_ok=True)

#     # Read video
#     cap = cv2.VideoCapture(video_path)
#     frame_skip = 5   # process every 5th frame
#     frame_count = 0
#     saved_frames = 0
#     max_frames = 20  # return up to 20 images

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         frame_count += 1

#         # skip frames
#         if frame_count % frame_skip != 0:
#             continue

#         # run YOLO detection
#         results = model(frame)

#         # if any detection → save frame
#         if len(results[0].boxes) > 0:
#             output_path = os.path.join(frame_output_dir, f"{file_id}_{frame_count}.jpg")
#             cv2.imwrite(output_path, results[0].plot())
#             saved_frames += 1

#         if saved_frames >= max_frames:
#             break

#     cap.release()

#     # If no frames found
#     if saved_frames == 0:
#         return {"message": "No detections found in video"}

#     # Create a ZIP file of detected frames
#     zip_path = os.path.join(ZIP_FOLDER, f"{file_id}.zip")
#     with zipfile.ZipFile(zip_path, 'w') as zipf:
#         for img_name in os.listdir(frame_output_dir):
#             img_path = os.path.join(frame_output_dir, img_name)
#             zipf.write(img_path, img_name)

#     return FileResponse(zip_path, media_type="application/zip", filename="detected_frames.zip")


# // zip


# import cv2
# import zipfile
# import shutil
# from fastapi import FastAPI, UploadFile, File
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import FileResponse, StreamingResponse
# from ultralytics import YOLO
# import os
# import uuid

# app = FastAPI()

# # -------------------------------
# # CORS (allow React frontend)
# # -------------------------------
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # -------------------------------
# # Load YOLOv8 model
# # -------------------------------
# model = YOLO("model/best.pt")

# # -------------------------------
# # Folder setup
# # -------------------------------
# UPLOAD_FOLDER = "uploads"
# FRAMES_FOLDER = "output_frames"
# ZIP_FOLDER = "zip_output"

# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(FRAMES_FOLDER, exist_ok=True)
# os.makedirs(ZIP_FOLDER, exist_ok=True)

# # =====================================================================
# # 🟦 1. VIDEO UPLOAD → RETURN 20 DETECTED FRAMES (ZIP)
# # =====================================================================
# @app.post("/detect-video/")
# async def detect_video(file: UploadFile = File(...)):
#     file_id = str(uuid.uuid4())

#     # Save uploaded video
#     file_ext = os.path.splitext(file.filename)[-1]
#     video_path = os.path.join(UPLOAD_FOLDER, f"{file_id}{file_ext}")

#     with open(video_path, "wb") as f:
#         f.write(await file.read())

#     # Output directory
#     frame_output_dir = os.path.join(FRAMES_FOLDER, file_id)
#     os.makedirs(frame_output_dir, exist_ok=True)

#     cap = cv2.VideoCapture(video_path)
#     frame_skip = 5
#     frame_count = 0
#     saved_frames = 0
#     max_frames = 20

#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         frame_count += 1
#         if frame_count % frame_skip != 0:
#             continue

#         # YOLO detection
#         results = model(frame)

#         if len(results[0].boxes) > 0:
#             output_path = os.path.join(frame_output_dir, f"{file_id}_{frame_count}.jpg")
#             cv2.imwrite(output_path, results[0].plot())
#             saved_frames += 1

#         if saved_frames >= max_frames:
#             break

#     cap.release()

#     if saved_frames == 0:
#         return {"message": "No detections found in the video"}

#     # Create ZIP of detection frames
#     zip_path = os.path.join(ZIP_FOLDER, f"{file_id}.zip")
#     with zipfile.ZipFile(zip_path, "w") as zipf:
#         for img_name in os.listdir(frame_output_dir):
#             zipf.write(os.path.join(frame_output_dir, img_name), img_name)

#     return FileResponse(zip_path, media_type="application/zip", filename="detected_frames.zip")


# # =====================================================================
# # 🟩 2. LIVE YOLO CAMERA DETECTION → STREAM TO REACT
# # =====================================================================
# @app.get("/live-detect/")
# def live_detect():
#     cap = cv2.VideoCapture(0)  # Webcam index

#     def generate_frames():
#         while True:
#             ret, frame = cap.read()
#             if not ret:
#                 break

#             results = model(frame)
#             processed_frame = results[0].plot()

#             ret, jpeg = cv2.imencode(".jpg", processed_frame)
#             if not ret:
#                 continue

#             frame_bytes = jpeg.tobytes()

#             yield (
#                 b"--frame\r\n"
#                 b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
#             )

#     return StreamingResponse(
#         generate_frames(),
#         media_type="multipart/x-mixed-replace; boundary=frame"
#     )


# # =====================================================================
# # 🟧 3. OPTIONAL: BASIC IMAGE/VIDEO DETECTION (RETURNS SINGLE OUTPUT)
# # =====================================================================
# @app.post("/detect/")
# async def detect(file: UploadFile = File(...)):
#     file_ext = os.path.splitext(file.filename)[1]
#     file_id = str(uuid.uuid4()) + file_ext
#     input_path = os.path.join(UPLOAD_FOLDER, file_id)

#     with open(input_path, "wb") as f:
#         f.write(await file.read())

#     results = model.predict(source=input_path, save=True, project="runs/detect", name=file_id)
#     output_dir = os.path.join("runs/detect", file_id)
#     saved_files = os.listdir(output_dir)

#     if not saved_files:
#         return {"error": "No output generated"}

#     output_file = saved_files[0]
#     output_path = os.path.join(output_dir, output_file)

#     media_type = "video/mp4" if output_file.endswith(".mp4") else "image/jpeg"

#     return FileResponse(output_path, media_type=media_type)



import cv2
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from ultralytics import YOLO
import os
import uuid
import time

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

# -------------------------------
# CORS (allow React frontend)
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # you can restrict to ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Load YOLOv8 model
# -------------------------------
import pathlib
base_dir = pathlib.Path(__file__).parent
model_path = base_dir / "model/best.pt"
model = YOLO(str(model_path))   # adjust path if needed

# -------------------------------
# Folder setup
# -------------------------------
# Folder setup
# -------------------------------
UPLOAD_FOLDER = base_dir / "uploads"
FRAMES_FOLDER = base_dir / "output_frames"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(FRAMES_FOLDER, exist_ok=True)

# Serve detected frames as static files
# URL: http://127.0.0.1:8000/output_frames/<file_id>/<image_name>.jpg
app.mount("/output_frames", StaticFiles(directory=FRAMES_FOLDER), name="output_frames")


# =====================================================================
# 🟦 1. VIDEO UPLOAD → RETURN ~20 DETECTED FRAMES (AS URLs)
# =====================================================================
@app.post("/detect-video/")
async def detect_video(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())

    # Save uploaded video
    file_ext = os.path.splitext(file.filename)[-1]
    video_path = os.path.join(UPLOAD_FOLDER, f"{file_id}{file_ext}")

    with open(video_path, "wb") as f:
        f.write(await file.read())

    # Output directory for this video's frames
    frame_output_dir = os.path.join(FRAMES_FOLDER, file_id)
    os.makedirs(frame_output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    frame_skip = 5          # process every 5th frame
    frame_count = 0
    saved_frames = 0
    max_frames = 20         # cap number of frames returned

    image_urls = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        # Skip frames to reduce computation
        if frame_count % frame_skip != 0:
            continue

        # YOLO detection
        results = model(frame)

        # If any detection present -> save this frame
        if len(results[0].boxes) > 0:
            img_name = f"{file_id}_{frame_count}.jpg"
            img_path = os.path.join(frame_output_dir, img_name)
            cv2.imwrite(img_path, results[0].plot())
            saved_frames += 1

            # Build URL for frontend to load this image
            url = f"http://127.0.0.1:8000/output_frames/{file_id}/{img_name}"
            image_urls.append(url)

        if saved_frames >= max_frames:
            break

    cap.release()

    if not image_urls:
        return {"message": "No detections found in the video", "images": []}

    # Return list of detection frame URLs
    return {"images": image_urls}


# =====================================================================
# 🟩 2. LIVE YOLO CAMERA DETECTION → STREAM TO REACT
# =====================================================================
# Global flag to control camera loop
camera_running = False

@app.post("/stop-live/")
def stop_live():
    global camera_running
    camera_running = False
    print("Stop signal received. Stopping camera...", flush=True)
    return {"message": "Camera stopping"}

@app.get("/live-detect/")
def live_detect(camera_id: int = 1):
    global camera_running
    camera_running = True
    
    print(f"Initializing camera {camera_id}...", flush=True)
    cap = cv2.VideoCapture(camera_id)  # User requested index 1
    
    # Set lower resolution for speed
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    if not cap.isOpened():
        print("Error: Could not open camera.", flush=True)
        return {"error": "Could not open camera"}

    def generate_frames():
        global camera_running
        frame_count = 0
        try:
            while camera_running:
                ret, frame = cap.read()
                if not ret:
                    print("Error: Failed to read frame from camera.", flush=True)
                    break
                
                frame_count += 1
                
                # Skip frames: Process every 3rd frame (approx 10 FPS)
                if frame_count % 3 != 0:
                    continue

                # Resize to improve inference speed on CPU
                frame = cv2.resize(frame, (640, 480))

                # Add timestamp
                cv2.putText(frame, f"Live: {time.ctime()}", (10, 30), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

                # Run YOLO
                results = model(frame, verbose=False)
                processed_frame = results[0].plot()

                # Encode as JPEG
                ret_jpeg, jpeg = cv2.imencode(".jpg", processed_frame)
                if not ret_jpeg:
                    continue

                frame_bytes = jpeg.tobytes()

                # MJPEG stream chunk
                yield (
                    b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n"
                )
        except Exception as e:
            print(f"Streaming error: {e}", flush=True)
        finally:
            print("Releasing camera...", flush=True)
            cap.release()
            camera_running = False

    return StreamingResponse(
        generate_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )


# =====================================================================
# 🟧 3. BASIC IMAGE/VIDEO DETECTION → RETURN SINGLE OUTPUT FILE
# =====================================================================
# @app.post("/detect/")
# async def detect(file: UploadFile = File(...)):
#     file_ext = os.path.splitext(file.filename)[1]
#     file_id = str(uuid.uuid4()) + file_ext
#     input_path = os.path.join(UPLOAD_FOLDER, file_id)

#     # Save uploaded file
#     with open(input_path, "wb") as f:
#         f.write(await file.read())

#     # Run YOLO prediction
#     results = model.predict(
#         source=input_path,
#         save=True,
#         project="runs/detect",
#         name=file_id
#     )

#     # YOLO saves results to runs/detect/<file_id>/
#     output_dir = os.path.join("runs/detect", file_id)
#     saved_files = os.listdir(output_dir) if os.path.exists(output_dir) else []

#     if not saved_files:
#         return {"error": "No output generated"}

#     output_file = saved_files[0]
#     output_path = os.path.join(output_dir, output_file)

#     # Decide type
#     media_type = "video/mp4" if output_file.endswith(".mp4") else "image/jpeg"

#     return FileResponse(output_path, media_type=media_type)


    # =====================================================================
# 🟨 IMAGE UPLOAD → RETURN DETECTED IMAGE PREVIEW
# =====================================================================
@app.post("/detect-image/")
async def detect_image(file: UploadFile = File(...)):
    file_ext = os.path.splitext(file.filename)[-1].lower()
    file_id = str(uuid.uuid4()) + file_ext
    input_path = os.path.join(UPLOAD_FOLDER, file_id)

    # Save uploaded image
    with open(input_path, "wb") as f:
        f.write(await file.read())

    # YOLO detect & save results
    results = model.predict(
        source=input_path,
        save=True,
        project="runs/image_detect",
        name=file_id
    )

    output_dir = os.path.join("runs/image_detect", file_id)
    saved_files = os.listdir(output_dir)

    if not saved_files:
        return {"error": "No detections found"}

    output_image = saved_files[0]
    output_path = os.path.join(output_dir, output_image)

    return FileResponse(output_path, media_type="image/jpeg")

