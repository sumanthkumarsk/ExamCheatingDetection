import cv2
import time

print("Testing camera access...")
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera (index 0).")
    exit(1)

print("Camera opened successfully.")
ret, frame = cap.read()
if ret:
    print(f"Frame captured. Size: {frame.shape}")
else:
    print("Error: Could not read frame.")

print("Releasing camera.")
cap.release()
print("Done.")
