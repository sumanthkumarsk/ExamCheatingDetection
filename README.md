# CheatGuard - AI Student Monitoring System

**CheatGuard** is an advanced AI-powered proctoring application designed to detect suspicious activities during examinations. It uses **YOLOv8** for real-time object detection and supports **Live Webcam Monitoring**, **Video Analysis**, and **Image Auditing**.

---

## 🚀 Features

*   **Live Proctoring**: Real-time detection of mobile phones, head rotations, hand gestures, and paper passing using the webcam.
*   **Video Analysis**: Upload exam footage to detect and flag anomalies frame-by-frame.
*   **Image Audit**: Analyze static snapshots for prohibited items.
*   **Premium UI**: A cyber-security themed, responsive dashboard built with React and Tailwind CSS.

---

## 🛠️ Tech Stack

*   **Backend**: Python, FastAPI, Ultralytics YOLOv8, OpenCV
*   **Frontend**: React (Vite), Tailwind CSS, Framer Motion, Axios

---

## 📋 Prerequisites

Ensure you have the following installed:
*   **Python 3.9+**
*   **Node.js 16+** & **npm**

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd student-monitoring-yolov8
```

### 2. Backend Setup (FastAPI)
The backend processes video feeds and runs the YOLOv8 model.

1.  Navigate to the directory:
    ```bash
    cd backend
    ```
2.  Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Important**: Ensure your YOLO model file is placed correctly:
    *   Place `best.pt` inside `backend/model/best.pt`.

### 3. Frontend Setup (React)
The frontend provides the user interface.

1.  Navigate to the frontend directory:
    ```bash
    cd ../frontend/vite-project
    ```
2.  Install Node dependencies:
    ```bash
    npm install
    ```

---

## ▶️ Running the Application

You need to run the Backend and Frontend in **two separate terminals**.

### Terminal 1: Start Backend
```bash
cd backend
uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```
*   The backend will start at `http://127.0.0.1:8000`.

### Terminal 2: Start Frontend
```bash
cd frontend/vite-project
npm run dev
```
*   The frontend will start at `http://localhost:5173`.
*   **Ctrl + Click** the link to open it in your browser.

---

## 🔍 Usage Guide

1.  **Dashboard**: You will see the CheatGuard dashboard with status "System Operational".
2.  **Live Monitor**:
    *   Click **Start Protection** to enable the webcam.
    *   The system will detect behaviors like "Phone", "Head Rotation", etc.
    *   Click **Stop Monitoring** to end the session.
3.  **Video Analysis**:
    *   Go to the **Video Analysis** tab.
    *   Upload a video file (`.mp4`, `.mov`).
    *   Click **Run Video Audit**.
    *   Detected anomalous frames will be displayed below.
4.  **Image Audit**:
    *   Upload an image to get an instant analysis report.

---

## 📂 Project Structure

```
student-monitoring-yolov8/
├── backend/
│   ├── app.py              # Main API Logic
│   ├── requirements.txt    # Python dependencies
│   └── model/
│       └── best.pt         # YOLOv8 Model Weights
└── frontend/
    └── vite-project/
        ├── src/
        │   ├── App.jsx     # Main React Component
        │   └── App.css     # Styles
        └── package.json    # Node dependencies
```

---

## ⚠️ Common Issues

*   **"Backend Disconnected"**: Ensure the backend terminal is running and reachable at port 8000.
*   **Camera Not Starting**: Check if another app (like Zoom/Teams) is using the camera. Using a browser on a different machine? The backend runs locally, so the camera must be connected to the *server* machine.
*   **Module Not Found (Vite)**: If you see errors about "rollup" or "paths", ensure you didn't name your folders with spaces (e.g., `7th SEM` -> `7th_SEM`), or just try re-installing user `npm install`.

---
&copy; 2026 CheatGuard Inc.
