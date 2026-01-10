// import React, { useState } from "react";
// import axios from "axios";
// import "./App.css";

// function App() {
//   const [file, setFile] = useState(null);
//   const [output, setOutput] = useState(null);
//   const [mimeType, setMimeType] = useState(null);
//   const [loading, setLoading] = useState(false);

// const handleDetect = async (e) => {
//   e.preventDefault();

//   if (!file) return alert("Please upload a file!");

//   setLoading(true);
//   setOutput(null);

//   const formData = new FormData();
//   formData.append("file", file);

//   try {
//     const response = await axios.post(
//       "http://127.0.0.1:8000/detect/",
//       formData,
//       { responseType: "blob" }
//     );

//     const mime = response.data.type;
//     const url = URL.createObjectURL(new Blob([response.data], { type: mime }));

//     setOutput(url);
//     setMimeType(mime);

//   } catch (error) {
//     alert("Error detecting file!");
//     console.error(error);
//   } finally {
//     setLoading(false);
//   }
// };


//   const handleDetect = async (e) => {
//   e.preventDefault();

//   if (!file) return alert("Please upload a file!");

//   setLoading(true);

//   const formData = new FormData();
//   formData.append("file", file);

//   const response = await axios.post(
//     "http://127.0.0.1:8000/detect-video/",
//     formData,
//     { responseType: "blob" }
//   );

//  const fileURL = URL.createObjectURL(response.data);
//   setOutput(fileURL);
//   setLoading(false);
// };


//   return (
//     <div className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-black text-white flex flex-col items-center p-6">

//       <h1 className="text-5xl font-extrabold mt-8 mb-10 bg-clip-text text-transparent 
//                      bg-gradient-to-r from-blue-400 to-purple-500 drop-shadow-lg">
//         YOLOv8 Student Monitoring
//       </h1>

//       {/* Upload Card */}
//       <div className="backdrop-blur-xl bg-white/10 p-8 rounded-2xl shadow-2xl border border-white/10 w-full max-w-lg transition duration-300 hover:bg-white/20">
//         <form onSubmit={handleDetect} className="flex flex-col items-center gap-6">

//           <label className="w-full">
//             <div className="w-full h-40 border-2 border-dashed border-blue-400 rounded-xl flex flex-col justify-center items-center 
//                             bg-white/5 hover:bg-white/10 transition cursor-pointer">
//               <span className="text-lg">Click or Drag & Drop File</span>
//               <span className="text-sm text-gray-300 mt-1">(Image or Video)</span>
//             </div>
//             <input 
//               type="file"
//               accept="image/*,video/*"
//               className="hidden"
//               onChange={(e) => setFile(e.target.files[0])}
//             />
//           </label>

//           <button
//             type="submit"
//             className="w-full bg-gradient-to-r from-blue-600 to-purple-600 py-3 rounded-xl 
//                        hover:scale-[1.02] transition font-semibold shadow-lg text-lg"
//           >
//             Detect
//           </button>
//         </form>
//       </div>

//       {/* Loading Animation */}
//       {loading && (
//         <div className="mt-8">
//           <div className="animate-spin w-12 h-12 border-4 border-blue-500 border-t-transparent rounded-full"></div>
//           <p className="mt-4 text-lg font-medium">Processing...</p>
//         </div>
//       )}

//       {/* Output Preview */}
//       {output && (
//   <div className="mt-10 backdrop-blur-xl bg-white/10 p-6 rounded-2xl border border-white/10 shadow-xl max-w-2xl text-center">
//     <h2 className="text-2xl font-bold mb-4 text-blue-300">
//       Detection Result (Download Frames)
//     </h2>

//     <a
//       href={output}
//       download="detected_frames.zip"
//       className="inline-block bg-blue-600 hover:bg-blue-500 text-white font-semibold px-6 py-3 rounded-xl shadow-lg transition-all duration-300"
//     >
//       ⬇ Download Detected Frames (ZIP)
//     </a>

//     <p className="text-sm text-blue-200 mt-4">
//       Contains 10–20 detected images from your video.
//     </p>
//   </div>
// )}


//     </div>
//   );
// }

// export default App;



// zip



// import React, { useState } from "react";
// import axios from "axios";
// import "./App.css";

// function App() {
//   const [file, setFile] = useState(null);
//   const [output, setOutput] = useState(null);
//   const [loading, setLoading] = useState(false);

//   // -----------------------------
//   // 📌 HANDLE VIDEO → ZIP DETECTION
//   // -----------------------------
//   const handleDetect = async (e) => {
//     e.preventDefault();

//     if (!file) return alert("Please upload a file!");

//     setLoading(true);
//     setOutput(null);

//     const formData = new FormData();
//     formData.append("file", file);

//     try {
//       const response = await axios.post(
//         "http://127.0.0.1:8000/detect-video/",
//         formData,
//         { responseType: "blob" }
//       );

//       const url = URL.createObjectURL(response.data);
//       setOutput(url);
//     } catch (error) {
//       console.error(error);
//       alert("Error processing video");
//     }

//     setLoading(false);
//   };

//   return (
//     <div className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-black text-white flex flex-col items-center p-6">

//       {/* Title */}
//       <h1 className="text-5xl font-extrabold mt-8 mb-10 bg-clip-text text-transparent 
//                      bg-gradient-to-r from-blue-400 to-purple-500 drop-shadow-lg">
//         YOLOv8 Student Monitoring
//       </h1>

//       {/* ----------------------------- */}
//       {/* 📂 UPLOAD CARD */}
//       {/* ----------------------------- */}
//       <div className="backdrop-blur-xl bg-white/10 p-8 rounded-2xl shadow-2xl border border-white/10 w-full max-w-lg transition duration-300 hover:bg-white/20">
//         <form onSubmit={handleDetect} className="flex flex-col items-center gap-6">

//           <label className="w-full cursor-pointer">
//             <div className="w-full h-40 border-2 border-dashed border-blue-400 rounded-xl flex flex-col justify-center items-center 
//                             bg-white/5 hover:bg-white/10 transition">
//               <span className="text-lg">Click or Drag & Drop File</span>
//               <span className="text-sm text-gray-300 mt-1">(Upload Video)</span>
//             </div>
//             <input 
//               type="file"
//               accept="video/*"
//               className="hidden"
//               onChange={(e) => setFile(e.target.files[0])}
//             />
//           </label>

//           <button
//             type="submit"
//             className="w-full bg-gradient-to-r from-blue-600 to-purple-600 py-3 rounded-xl 
//                        hover:scale-[1.02] transition font-semibold shadow-lg text-lg"
//           >
//             Detect Video
//           </button>
//         </form>
//       </div>

//       {/* ----------------------------- */}
//       {/* ⏳ LOADING ANIMATION */}
//       {/* ----------------------------- */}
//       {loading && (
//         <div className="mt-8">
//           <div className="animate-spin w-12 h-12 border-4 border-blue-500 border-t-transparent rounded-full"></div>
//           <p className="mt-4 text-lg font-medium">Processing...</p>
//         </div>
//       )}

//       {/* ----------------------------- */}
//       {/* 📦 ZIP OUTPUT DOWNLOAD */}
//       {/* ----------------------------- */}
//       {output && (
//         <div className="mt-10 backdrop-blur-xl bg-white/10 p-6 rounded-2xl border border-white/10 shadow-xl max-w-2xl text-center">
//           <h2 className="text-2xl font-bold mb-4 text-blue-300">
//             Detection Result (Download Frames)
//           </h2>

//           <a
//             href={output}
//             download="detected_frames.zip"
//             className="inline-block bg-blue-600 hover:bg-blue-500 text-white font-semibold px-6 py-3 rounded-xl shadow-lg transition-all duration-300"
//           >
//             ⬇ Download Detected Frames (ZIP)
//           </a>

//           <p className="text-sm text-blue-200 mt-4">
//             Contains ~20 detected images from your video.
//           </p>
//         </div>
//       )}

//       {/* ----------------------------- */}
//       {/* 🎥 LIVE CAMERA YOLO DETECTION */}
//       {/* ----------------------------- */}
//       <div className="mt-16 backdrop-blur-xl bg-white/10 p-6 rounded-2xl border border-white/10 shadow-xl max-w-2xl w-full text-center">
//         <h2 className="text-2xl font-bold mb-4 text-green-300">
//           Live Camera Detection
//         </h2>

//         <img
//           src="http://127.0.0.1:8000/live-detect/"
//           alt="Live YOLO detection"
//           className="rounded-xl w-full shadow-xl"
//         />

//         <p className="text-sm text-green-200 mt-4">
//           Real-time camera stream processed by YOLOv8.
//         </p>
//       </div>

//     </div>
//   );
// }

// export default App;




import React, { useState } from "react";
import axios from "axios";
import { motion, AnimatePresence } from "framer-motion";
import {
  ShieldCheck,
  Camera,
  Upload,
  Video,
  Image as ImageIcon,
  AlertTriangle,
  Eye,
  Smartphone,
  Headphones,
  FileText,
  Hand,
  Activity
} from "lucide-react";
import "./App.css";

function App() {
  const [activeTab, setActiveTab] = useState("live");
  const [file, setFile] = useState(null);
  const [imageOutput, setImageOutput] = useState(null);
  const [frames, setFrames] = useState([]);
  const [loading, setLoading] = useState(false);
  const [isLiveActive, setIsLiveActive] = useState(false);
  const [isCameraLoading, setIsCameraLoading] = useState(false);
  const [systemStatus, setSystemStatus] = useState("disconnected");

  // -----------------------------
  // SYSTEM HEALTH CHECK
  // -----------------------------
  React.useEffect(() => {
    const checkHealth = async () => {
      try {
        await axios.get("http://127.0.0.1:8000/health");
        setSystemStatus("operational");
      } catch (e) {
        setSystemStatus("disconnected");
      }
    };

    checkHealth();
    const interval = setInterval(checkHealth, 5000); // Check every 5s
    return () => clearInterval(interval);
  }, []);

  // -----------------------------
  // API HANDLERS
  // -----------------------------
  const handleDetectImage = async () => {
    if (!file) return alert("Upload an image!");
    setLoading(true);
    setImageOutput(null);
    setFrames([]);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/detect-image/",
        formData,
        { responseType: "blob" }
      );
      const imgUrl = URL.createObjectURL(response.data);
      setImageOutput(imgUrl);
    } catch (e) {
      console.error(e);
      alert("Error detecting image");
    }
    setLoading(false);
  };

  const handleDetectVideo = async () => {
    if (!file) return alert("Upload a video!");
    setLoading(true);
    setImageOutput(null);
    setFrames([]);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/detect-video/",
        formData
      );
      if (response.data.images?.length > 0) {
        setFrames(response.data.images);
      } else {
        alert("No detections found!");
      }
    } catch (e) {
      console.error(e);
      alert("Error detecting video");
    }
    setLoading(false);
  };

  const stopLiveCamera = async () => {
    try {
      await axios.post("http://127.0.0.1:8000/stop-live/");
    } catch (e) {
      console.error("Stop failed", e);
    }
    setIsLiveActive(false);
    setIsCameraLoading(false);
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-200 font-sans selection:bg-emerald-500/30">

      {/* ----------------------------- */}
      {/* HEADER */}
      {/* ----------------------------- */}
      <nav className="w-full backdrop-blur-md bg-slate-950/80 border-b border-slate-800 sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-6 h-20 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="bg-gradient-to-tr from-emerald-500 to-cyan-500 p-2 rounded-lg shadow-lg shadow-emerald-500/20">
              <ShieldCheck className="w-6 h-6 text-white" />
            </div>
            <span className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-emerald-400 to-cyan-400 tracking-wide">
              CheatGuard
            </span>
          </div>
          <div className="hidden md:flex items-center gap-6 text-sm font-medium text-slate-400">
            {systemStatus === "operational" ? (
              <span className="flex items-center gap-2 text-emerald-400">
                <Activity className="w-4 h-4" /> System Operational
              </span>
            ) : (
              <span className="flex items-center gap-2 text-red-500 animate-pulse">
                <AlertTriangle className="w-4 h-4" /> Backend Disconnected
              </span>
            )}
            <span className="text-slate-600">|</span>
            <span>v1.0.4</span>
          </div>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto px-6 py-12">

        {/* ----------------------------- */}
        {/* HERO SECTION */}
        {/* ----------------------------- */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6 }}
          className="text-center mb-16"
        >
          <h1 className="text-5xl md:text-6xl font-extrabold text-white mb-6 leading-tight">
            Advanced AI <span className="text-emerald-400">Proctoring</span>
          </h1>
          <p className="text-lg text-slate-400 max-w-2xl mx-auto">
            Real-time examination integrity verification using YOLOv8.
            Detects suspicious behavior with high precision.
          </p>
        </motion.div>

        {/* ----------------------------- */}
        {/* FEATURE GRID */}
        {/* ----------------------------- */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2, duration: 0.6 }}
          className="grid grid-cols-2 md:grid-cols-5 gap-4 mb-20"
        >
          <FeatureCard icon={Eye} label="Head Rotation" />
          <FeatureCard icon={Hand} label="Hand Gestures" />
          <FeatureCard icon={Smartphone} label="Mobile Phone" />
          <FeatureCard icon={Headphones} label="Headphones" />
          <FeatureCard icon={FileText} label="Paper Passing" />
        </motion.div>

        {/* ----------------------------- */}
        {/* CONTROL PANEL (TABS) */}
        {/* ----------------------------- */}
        <div className="bg-slate-900/50 backdrop-blur-xl border border-slate-800 rounded-3xl p-2 max-w-4xl mx-auto shadow-2xl overflow-hidden">

          {/* Tab Navigation */}
          <div className="flex p-1 bg-slate-950/50 rounded-2xl mb-8">
            <TabButton
              active={activeTab === "live"}
              onClick={() => setActiveTab("live")}
              icon={Camera}
              label="Live Monitor"
            />
            <TabButton
              active={activeTab === "image"}
              onClick={() => setActiveTab("image")}
              icon={ImageIcon}
              label="Image Audit"
            />
            <TabButton
              active={activeTab === "video"}
              onClick={() => setActiveTab("video")}
              icon={Video}
              label="Video Analysis"
            />
          </div>

          {/* Tab Content */}
          <div className="p-6 md:p-8 min-h-[500px] flex flex-col items-center justify-center relative">

            <AnimatePresence mode="wait">

              {/* --- LIVE TAB --- */}
              {activeTab === "live" && (
                <motion.div
                  key="live"
                  initial={{ opacity: 0, scale: 0.95 }}
                  animate={{ opacity: 1, scale: 1 }}
                  exit={{ opacity: 0, scale: 0.95 }}
                  transition={{ duration: 0.3 }}
                  className="w-full flex flex-col items-center"
                >
                  <div className="relative w-full max-w-3xl aspect-video bg-black rounded-2xl overflow-hidden border-2 border-slate-800 shadow-2xl group flex justify-center items-center">
                    {isLiveActive ? (
                      <>
                        {isCameraLoading && (
                          <div className="absolute inset-0 flex flex-col items-center justify-center bg-black z-10">
                            <Activity className="w-12 h-12 text-emerald-500 animate-spin mb-4" />
                            <p className="text-emerald-400 font-mono animate-pulse">INITIALIZING CAMERA STREAM...</p>
                          </div>
                        )}
                        <img
                          src={`http://127.0.0.1:8000/live-detect/?t=${Date.now()}`}
                          alt="Live Stream"
                          className="w-full h-full object-contain"
                          onLoad={() => setIsCameraLoading(false)}
                          onError={() => {
                            alert("Connection lost. Stop and Start again.");
                            setIsLiveActive(false);
                            setIsCameraLoading(false);
                          }}
                        />
                        <div className="absolute top-4 left-4 flex gap-2 z-20">
                          <span className="bg-red-600 animate-pulse w-3 h-3 rounded-full"></span>
                          <span className="text-red-500 font-mono font-bold text-xs">LIVE REC</span>
                        </div>
                      </>
                    ) : (
                      <div className="absolute inset-0 flex flex-col items-center justify-center text-slate-500">
                        <Camera className="w-16 h-16 mb-4 opacity-50" />
                        <p>Camera Feed Inactive</p>
                      </div>
                    )}
                  </div>

                  <div className="mt-8 flex gap-4">
                    {!isLiveActive ? (
                      <button
                        onClick={() => {
                          setIsLiveActive(true);
                          setIsCameraLoading(true);
                        }}
                        className="bg-emerald-500 hover:bg-emerald-400 text-slate-950 px-8 py-3 rounded-xl font-bold flex items-center gap-2 transition-all hover:scale-105 shadow-[0_0_20px_rgba(16,185,129,0.3)]"
                      >
                        <ShieldCheck className="w-5 h-5" /> Start Protection
                      </button>
                    ) : (
                      <button
                        onClick={stopLiveCamera}
                        className="bg-red-500 hover:bg-red-400 text-white px-8 py-3 rounded-xl font-bold flex items-center gap-2 transition-all hover:scale-105 shadow-[0_0_20px_rgba(239,68,68,0.3)]"
                      >
                        <AlertTriangle className="w-5 h-5" /> Stop Monitoring
                      </button>
                    )}
                  </div>
                </motion.div>
              )}

              {/* --- IMAGE TAB --- */}
              {activeTab === "image" && (
                <motion.div
                  key="image"
                  initial={{ opacity: 0, x: 20 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ opacity: 0, x: -20 }}
                  className="w-full max-w-2xl flex flex-col items-center"
                >
                  <UploadArea
                    type="image"
                    onFileChange={setFile}
                    loading={loading}
                    onUpload={handleDetectImage}
                    selectedFile={file}
                  />

                  {imageOutput && (
                    <motion.div
                      initial={{ opacity: 0, y: 20 }}
                      animate={{ opacity: 1, y: 0 }}
                      className="mt-8 p-2 bg-slate-800/50 rounded-2xl border border-slate-700"
                    >
                      <img src={imageOutput} className="rounded-xl max-h-[400px] shadow-lg" alt="Analysis" />
                    </motion.div>
                  )}
                </motion.div>
              )}

              {/* --- VIDEO TAB --- */}
              {activeTab === "video" && (
                <motion.div
                  key="video"
                  initial={{ opacity: 0, x: 20 }}
                  animate={{ opacity: 1, x: 0 }}
                  exit={{ opacity: 0, x: -20 }}
                  className="w-full max-w-4xl flex flex-col items-center"
                >
                  <UploadArea
                    type="video"
                    onFileChange={setFile}
                    loading={loading}
                    onUpload={handleDetectVideo}
                    selectedFile={file}
                  />

                  {frames.length > 0 && (
                    <motion.div
                      initial={{ opacity: 0, y: 20 }}
                      animate={{ opacity: 1, y: 0 }}
                      className="mt-10 w-full"
                    >
                      <h3 className="text-xl font-bold text-emerald-400 mb-6 flex items-center gap-2">
                        <AlertTriangle className="w-5 h-5" /> Detected Anomalies
                      </h3>
                      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                        {frames.map((src, i) => (
                          <div key={i} className="group relative rounded-lg overflow-hidden border border-slate-700 hover:border-emerald-500 transition-all cursor-pointer">
                            <img src={src} className="w-full h-auto object-cover" />
                            <div className="absolute inset-0 bg-black/50 opacity-0 group-hover:opacity-100 flex items-center justify-center transition-opacity">
                              <span className="text-xs font-mono text-emerald-300">Frame {i + 1}</span>
                            </div>
                          </div>
                        ))}
                      </div>
                    </motion.div>
                  )}
                </motion.div>
              )}

            </AnimatePresence>
          </div>
        </div>

      </main>

      {/* FOOTER */}
      <footer className="text-center py-8 text-slate-600 text-sm">
        <p>&copy; 2026 CheatGuard Inc. All Systems Secured.</p>
      </footer>
    </div>
  );
}

// -----------------------------
// SUB-COMPONENTS
// -----------------------------

function FeatureCard({ icon: Icon, label }) {
  return (
    <div className="bg-slate-900 border border-slate-800 p-6 rounded-2xl flex flex-col items-center gap-4 hover:bg-slate-800 transition-colors group cursor-default">
      <div className="p-3 bg-slate-950 rounded-xl group-hover:text-emerald-400 transition-colors text-slate-500">
        <Icon className="w-8 h-8" />
      </div>
      <span className="font-semibold text-slate-300 text-center">{label}</span>
    </div>
  );
}

function TabButton({ active, onClick, icon: Icon, label }) {
  return (
    <button
      onClick={onClick}
      className={`flex-1 flex items-center justify-center gap-2 py-3 rounded-xl transition-all duration-300 font-medium ${active
        ? "bg-slate-800 text-emerald-400 shadow-lg shadow-emerald-500/10"
        : "text-slate-500 hover:text-slate-300 hover:bg-slate-800/50"
        }`}
    >
      <Icon className="w-5 h-5" />
      <span className="hidden md:inline">{label}</span>
      {active && (
        <motion.div
          layoutId="activeTab"
          className="absolute inset-0 bg-slate-800 rounded-xl -z-10"
        />
      )}
    </button>
  );
}

function UploadArea({ type, onFileChange, loading, onUpload, selectedFile }) {
  const [preview, setPreview] = React.useState(null);

  React.useEffect(() => {
    if (selectedFile) {
      // Create preview URL
      const url = URL.createObjectURL(selectedFile);
      setPreview(url);
      // Clean up URL on unmount or file change
      return () => URL.revokeObjectURL(url);
    } else {
      setPreview(null);
    }
  }, [selectedFile]);

  return (
    <div className="w-full max-w-lg">
      <label className="block w-full h-64 border-2 border-dashed border-slate-700 hover:border-emerald-500/50 rounded-2xl flex flex-col items-center justify-center bg-slate-950/50 hover:bg-slate-900/50 transition-all cursor-pointer group relative overflow-hidden">

        {preview ? (
          <div className="absolute inset-0 w-full h-full">
            {type === 'video' ? (
              <video src={preview} className="w-full h-full object-contain" controls />
            ) : (
              <img src={preview} className="w-full h-full object-contain" />
            )}
            <div className="absolute top-2 right-2 bg-black/60 text-white text-xs px-2 py-1 rounded">
              Click to Change
            </div>
          </div>
        ) : (
          <>
            <Upload className="w-10 h-10 text-slate-600 group-hover:text-emerald-500 mb-4 transition-colors" />
            <span className="text-slate-400 font-medium group-hover:text-slate-200">
              Upload {type === 'image' ? 'Snapshot' : 'Footage'}
            </span>
            <span className="text-xs text-slate-600 mt-2">.JPG, .PNG / .MP4, .MOV</span>
          </>
        )}

        <input
          type="file"
          className="hidden"
          accept={type === 'image' ? "image/*" : "video/*"}
          onChange={(e) => onFileChange(e.target.files[0])}
        />
      </label>

      <button
        onClick={onUpload}
        disabled={loading || !selectedFile}
        className={`w-full mt-6 bg-gradient-to-r from-emerald-600 to-cyan-600 hover:from-emerald-500 hover:to-cyan-500 text-white py-3 rounded-xl font-bold shadow-lg shadow-emerald-500/20 transition-all active:scale-95 ${loading || !selectedFile ? "opacity-50 cursor-not-allowed" : ""}`}
      >
        {loading ? (
          <span className="flex items-center justify-center gap-2">
            <Activity className="animate-spin" /> Analyzing...
          </span>
        ) : (
          `Run ${type === 'image' ? 'Image' : 'Video'} Audit`
        )}
      </button>
    </div>
  );
}

export default App;

//cd student-monitoring-yolov8   cd frontend  cd vite-project  npm run dev
//cd student-monitoring-yolov8 cd backend uvicorn app:app --reload


