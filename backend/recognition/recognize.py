import cv2
import os
import sys
import json
import numpy as np
import tensorflow as tf

# Parent path add
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import config


def load_labels():
    """Load label map from JSON file"""
    with open(config.LABELS_PATH, "r") as f:
        label_map = json.load(f)
    # Reverse map (id -> name)
    id_to_label = {v: k for k, v in label_map.items()}
    return id_to_label


def recognize():
    # Load trained model
    print("📂 Loading model...")
    model = tf.keras.models.load_model(config.MODEL_PATH)
    id_to_label = load_labels()

    # Start webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Camera not accessible!")
        return

    print("✅ Model loaded. Starting real-time recognition... Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame -> face detection (simple Haar Cascade)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            face_resized = cv2.resize(face, (config.IMG_SIZE, config.IMG_SIZE))
            face_norm = face_resized.astype("float32") / 255.0
            face_input = np.expand_dims(face_norm, axis=0)

            # Prediction
            preds = model.predict(face_input, verbose=0)[0]
            label_id = np.argmax(preds)
            confidence = preds[label_id]

            name = id_to_label[label_id] if confidence > 0.7 else "Unknown"

            # Draw bounding box
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f"{name} ({confidence*100:.1f}%)", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow("Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    recognize()


