# Real-Time Face Recognition Backend

This is the **backend** service for the **Real-Time Face Recognition WebApp**.
It is built with **FastAPI** and uses a **CNN (MobileNet) model** for recognizing faces in real-time.

The backend handles:

Collecting face images for new users
Training a deep learning model
Running recognition in real-time
Serving predictions via REST API for the React frontend

📂 Project Structure
~~~text
backend/
├── app.py                     # Main FastAPI app
├── config.py                  # Configuration settings
├── requirements.txt           # Python dependencies

├── data_collection/
│   └── collect.py             # Script to collect face images

├── dataset/
│   └── .gitkeep               # Placeholder for collected data

├── haarcascade/
│   └── haarcascade_frontalface_default.xml  # Haar Cascade for face detection

├── recognition/
│   └── recognize.py           # Recognition logic

├── saved_models/
│   ├── face_recognition_mobilenet.h5   # Trained CNN model (MobileNet)
│   └── labels.json            # Label mappings for recognized classes

├── training/
│   └── train_model.py         # Script to train/update the model
└── README.md                # Documentation
~~~

⚙️ Setup Instructions
1. Clone the Repository

  ```bash  
  git clone https://github.com/urwanarjis1/Real-Time-Face-Recognition-WebApp.git

  ```bash
  cd Real-Time-Face-Recognition-WebApp/backend

