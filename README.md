# Real-Time Face Recognition WebApp

This is a full-stack application for real-time face recognition.
It has two parts:

**Backend (FastAPI + CNN/MobileNet)** → Handles face data collection, training, recognition, and REST API.

**Frontend (React.js)** → Provides an interactive UI to register users, train models, and perform recognition.

**Python Version**: 3.9.23 ✅ Compatible with all backend dependencies.

**🚀 Features**

* Real-time face recognition using webcam
* User registration with face data
* Model training with collected dataset
* REST API (FastAPI) for recognition & user management
* React.js frontend with clean UI

**📂 Project Structure**
~~~text
Real-Time-Face-Recognition-WebApp/
├── backend/        # FastAPI + CNN Model
├── frontend/       # React.js UI
└── README.md       # Main project documentation
~~~

**⚙️ Setup Instructions**

1. **Clone the Repository**
  ```bash 
  git clone https://github.com/urwanarjis1/Real-Time-Face-Recognition-WebApp.git
  cd Real-Time-Face-Recognition-WebApp
  ```
2. **Backend Setup**
  ```bash 
  cd backend
  python -m venv venv
  venv\Scripts\activate        # On Windows
  source venv/bin/activate     # On Mac/Linux

  pip install -r requirements.txt
  uvicorn app:app --reload
  ```
Backend runs on → http://127.0.0.1:8000

3. **Frontend Setup**

  ```bash 
  cd frontend
  npm install
  npm start
  ```
Frontend runs on → http://localhost:3000

**🔗 API Endpoints (Backend)**

* POST /predict → Recognize user from an image
* GET /labels → Get all registered users
* POST /add-user → Register a new user

**📌 Notes**

* Run backend before starting the frontend
* Train the model after adding new users
* Ensure webcam access is allowed in the browser

Detailed setup & usage can be found in the individual backend/README.md and frontend/README.md

# License

This project is licensed under the MIT License – see the LICENSE file for details.