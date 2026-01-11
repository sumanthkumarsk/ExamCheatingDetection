import cv2
import time

def test_camera(index):
    print(f"Testing Camera {index}...", flush=True)
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        print(f"[-] Camera {index} failed to open.", flush=True)
        return False
    
    ret, frame = cap.read()
    if ret:
        print(f"[+] Camera {index} working! Frame size: {frame.shape}", flush=True)
        cap.release()
        return True
    else:
        print(f"[-] Camera {index} opened but returned no frame.", flush=True)
        cap.release()
        return False

if __name__ == "__main__":
    print("Enumerating cameras...", flush=True)
    found = False
    for i in range(5):
        if test_camera(i):
            found = True
    
    if not found:
        print("CRITICAL: No working cameras found on this system.", flush=True)
