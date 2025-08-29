import React, { useRef, useState, useEffect } from "react";
import axios from "axios";
import './Register.css'

function Register() {
  const videoRef = useRef(null);
  const [name, setName] = useState("");
  const [count, setCount] = useState(0);
  const [isCapturing, setIsCapturing] = useState(false);

  useEffect(() => {
    // Camera access
    navigator.mediaDevices
      .getUserMedia({ video: true })
      .then((stream) => {
        videoRef.current.srcObject = stream;
      })
      .catch((err) => console.error("Camera error: ", err));
  }, []);

  // Function: Capture Frame & Send
  const captureAndSend = async () => {
    if (!name) {
      alert("Please enter a name first!");
      return;
    }

    const canvas = document.createElement("canvas");
    canvas.width = 224; // tumhara IMG_SIZE
    canvas.height = 224;
    const ctx = canvas.getContext("2d");
    ctx.drawImage(videoRef.current, 0, 0, canvas.width, canvas.height);

    canvas.toBlob(async (blob) => {
      const formData = new FormData();
      formData.append("name", name);
      formData.append("file", blob, `${name}_${count + 1}.jpg`);

      try {
        const res = await axios.post("http://127.0.0.1:8000/register", formData, {
          headers: { "Content-Type": "multipart/form-data" },
        });

        if (res.data.count) {
          setCount(res.data.count);
        }
      } catch (err) {
        console.error("Upload error:", err);
      }
    }, "image/jpeg");
  };

  // Function: Start Auto Capture
  const startCapture = () => {
    if (!name) {
      alert("Enter name before capturing!");
      return;
    }
    setIsCapturing(true);

    const interval = setInterval(() => {
      setCount((prev) => {
        if (prev >= 200) {
          clearInterval(interval);
          setIsCapturing(false);
          alert("200 images captured!");
          return prev;
        }
        captureAndSend();
        return prev;
      });
    }, 1000); // ✅ every 1 second
  };

  return (
    <div className="p-6 text-center">
      <h1 className="text-xl font-bold mb-4">Register New User</h1>
      <input
        type="text"
        placeholder="Enter your name"
        className="border p-2 mb-4"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <br />
      <video ref={videoRef} autoPlay playsInline width="300" className="border rounded mb-4"></video>
      <br />
      <button
        onClick={startCapture}
        disabled={isCapturing}
        //className="bg-blue-500 text-white px-4 py-2 rounded"
        className="btn-custom"
      >
        {isCapturing ? "Capturing..." : "Start Capturing (200 images)"}
      </button>
      <p className="mt-4">Images Captured: {count} / 200</p>
    </div>
  );
}

export default Register;
