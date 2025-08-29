// Recognition.js
import React, { useRef, useState, useEffect } from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import './Recognition.css'
function Recognition() {
  const videoRef = useRef(null);
  const [result, setResult] = useState(null);

  useEffect(() => {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then((stream) => { videoRef.current.srcObject = stream; })
      .catch((err) => console.error("Camera error:", err));
  }, []);

  const captureAndSend = async () => {
    const canvas = document.createElement("canvas");
    canvas.width = 320;
    canvas.height = 240;
    canvas.getContext("2d").drawImage(videoRef.current, 0, 0, 320, 240);

    canvas.toBlob(async (blob) => {
      const formData = new FormData();
      formData.append("file", blob, "capture.jpg");

      try {
        const response = await fetch("http://127.0.0.1:8000/recognize/", {
          method: "POST",
          body: formData,
        });
        const data = await response.json();
        setResult(data);
      } catch (err) {
        console.error("Error sending image:", err);
      }
    }, "image/jpeg");
  };

  return (
    <div className="d-flex justify-content-center align-items-center min-vh-100" style={{backgroundColor: "#d1c4f0ff"}}>
      <div className="glass-card text-center">
        <h1 className="fw-bold mb-3">Face Recognition App</h1>
        <p>Capture your face & let AI recognize it instantly.</p>

        <div className="d-flex justify-content-center my-3">
          <video ref={videoRef} autoPlay width="320" height="240"/>
        </div>

        <button className="btn btn-custom btn-lg fw-bold" onClick={captureAndSend}>
          📷 Capture & Recognize
        </button>

        {result && (
          <div className="result-card text-center">
            <h4>✅ Prediction Result</h4>
            <p>
              <b>Name:</b> {result.name} <br />
              <b>Confidence:</b> {(result.confidence * 100).toFixed(2)}%
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

export default Recognition;
