# app.py
import io
import os
import json
import numpy as np
import cv2
import subprocess
from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import tensorflow as tf
import config

# ----------------- Paths -----------------
MODEL_PATH = "saved_models/face_recognition_mobilenet.h5"
LABELS_PATH = "saved_models/labels.json"
DATASET_DIR = "dataset"
MAX_IMAGES_PER_USER = 200

# ----------------- Load Model -----------------
model = tf.keras.models.load_model(MODEL_PATH)

# ----------------- Load Labels -----------------
with open(LABELS_PATH, "r") as f:
    label_map = json.load(f)
id_to_label = {v: k for k, v in label_map.items()}

# ----------------- Initialize FastAPI -----------------
app = FastAPI(title="Face Recognition API")

# Allow React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # production me specific origin set karna
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------- Utils -----------------
def preprocess_image(image_bytes: bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img = img.resize((224, 224))
    img_array = np.array(img).astype("float32") / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# ----------------- API Routes -----------------

# Recognition Route
@app.post("/recognize")
async def recognize(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        img_array = preprocess_image(contents)

        preds = model.predict(img_array, verbose=0)
        pred_id = int(np.argmax(preds, axis=1)[0])
        confidence = float(np.max(preds))

        if confidence < 0.7:
            name = "Unknown"
        else:
            name = id_to_label.get(pred_id, "Unknown")

        return JSONResponse({
            "predicted_id": pred_id,
            "name": name,
            "confidence": round(confidence, 4)
        })
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# Registration Route
@app.post("/register")
async def register(name: str = Form(...), file: UploadFile = File(...)):
    global model 
    try:
        user_dir = os.path.join(DATASET_DIR, name)
        os.makedirs(user_dir, exist_ok=True)

        count = len(os.listdir(user_dir))
        if count >= MAX_IMAGES_PER_USER:
            return JSONResponse({"message": "Limit reached (200 images)"})

        filename = f"{name}_{count+1}.jpg"
        filepath = os.path.join(user_dir, filename)

        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        img = cv2.resize(img, (config.IMG_SIZE, config.IMG_SIZE))
        cv2.imwrite(filepath, img)
        model = tf.keras.models.load_model(MODEL_PATH)
        return JSONResponse({"message": "Image saved successfully", "count": count + 1})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# Global model variable
model = tf.keras.models.load_model(MODEL_PATH)

@app.post("/train")
async def train_model():
    global model  # <-- important
    try:
        script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "training", "train_model.py"))
        subprocess.run(["python", script_path], check=True)
        
        # Training ke baad model reload karna
        model = tf.keras.models.load_model(MODEL_PATH)
        
        return JSONResponse({"message": "Training completed successfully, model reloaded"})
    except subprocess.CalledProcessError as e:
        return JSONResponse({"error": f"Training failed: {str(e)}"}, status_code=500)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


# ----------------- Run Server -----------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)



