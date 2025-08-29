import React, { useState } from "react";
import './Train.css'

function Train() {
  const [status, setStatus] = useState("");
  const [isTraining, setIsTraining] = useState(false);  // ✅ new state

  const handleTrain = async () => {
    setStatus("⏳ Training has started... Please wait.");
    setIsTraining(true);   // ✅ button disable

    try {
      const res = await fetch("http://127.0.0.1:8000/train", {
        method: "POST",
      });

      const data = await res.json();

      if (res.ok) {
        setStatus("✅ " + data.message);
      } else {
        setStatus("❌ " + (data.error || "Training failed"));
      }
    } catch (err) {
      setStatus("❌ Error: " + err.message);
    } finally {
      setIsTraining(false); // ✅ button enabled after training
    }
  };

  return (
    <div className="container">
      <h2>Train Model</h2>
      <button
        className="btn"
        onClick={handleTrain}
        disabled={isTraining}   // ✅ disable when training
      >
        {isTraining ? "Training..." : "Start Training"}
      </button>
      <p style={{ marginTop: "15px", fontWeight: "bold" }}>{status}</p>
    </div>
  );
}

export default Train;










