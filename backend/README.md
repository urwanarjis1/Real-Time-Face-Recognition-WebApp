# Real-Time Face Recognition Backend

This is the **backend** service for the **Real-Time Face Recognition WebApp**.
It is built with **FastAPI** and uses a **CNN (MobileNet) model** for recognizing faces in real-time.

The backend handles:

Collecting face images for new users
Training a deep learning model
Running recognition in real-time
Serving predictions via REST API for the React frontend

**📂 Project Structure**
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

**⚙️ Setup Instructions**
1. Clone the Repository

  ```bash  
  git clone https://github.com/urwanarjis1/Real-Time-Face-Recognition-WebApp.git
  ```

  ```bash
  cd Real-Time-Face-Recognition-WebApp/backend
  ```
2. Create Virtual Environment (Optional but Recommended)
   
  ```bash 
  python -m venv venv
  ```
  ```bash 
  source venv/bin/activate     # On Mac/Linux
  ```
  ```bash 
  venv\Scripts\activate        # On Windows
  ```

3. Install Dependencies

  ```bash 
  pip install -r requirements.txt
  ```

**🚀 Usage**

1. Start FastAPI Backend
  
  ```bash 
  uvicorn app:app --reload
  ```
   
Backend will run on http://127.0.0.1:8000 by default.
This connects with the React frontend for real-time face recognition.

2. Collect Face Data
  
  ```bash 
  python data_collection/collect.py
  ```

Use this to capture face images for new users. Images will be stored in dataset/.

3. Train the Model

  ```bash  
  python training/train_model.py
  ```
   
Trains/updates the CNN (MobileNet) model with collected face data.
Model will be saved in saved_models/.

4. Run Recognition
   
   ```bash 
  python recognition/recognize.py
  ```

Starts real-time recognition using webcam + trained MobileNet model.

**🔗 API Endpoints (FastAPI)**

POST /predict → Send an image and get the recognized user.

GET /labels → Fetch all available labels/classes.

POST /add-user → Collect data and add a new user.

**📌 Notes**

Ensure you have a webcam connected for data collection & recognition.
Train the model whenever you add new users.
This backend works together with the React frontend for live recognition.
