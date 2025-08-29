# Frontend - React Application

This is the **frontend** of the project, built using **React.js**.  
It provides the user interface and communicates with the backend API (Python/FastAPI).

---

 🚀 Features
- React.js based user interface
- Three main modules:
  - **Recognition** → Face recognition functionality
  - **Register** → Register new users with images
  - **Train** → Train the recognition model
- Responsive design with CSS styling
- Connects seamlessly with the backend API

---

📂 Project Structure
~~~text
frontend/
├── public/                  # Static files (index.html)
├── src/                     # React source code
│   ├── components/          # UI Components
│   │   ├── Recognition.css
│   │   ├── Recognition.js
│   │   ├── Register.css
│   │   ├── Register.js
│   │   ├── Train.css
│   │   └── Train.js
│   ├── App.css              # Global styles
│   ├── App.js               # Main app component
│   ├── App.test.js          # Sample test file
│   ├── index.css            # Styles for entry point
│   └── index.js             # React entry point
├── .gitignore               # Git ignore rules
├── package-lock.json        # Dependency lock file
├── package.json             # Project dependencies & scripts
└── README.md                # Documentation
~~~

---

 🛠️ Installation & Setup

1️⃣ Clone the repository

git clone https://github.com/your-username/your-repo.git
cd frontend

2️⃣ Install dependencies

  npm install

3️⃣ Run the development server
  
  npm start

The app will be available at: http://localhost:3000


📦 Build for Production

npm run build

This will generate optimized static files in the build/ folder.

🔗 Backend Connection

This frontend communicates with the Python FastAPI backend.
Make sure the backend server is running, then update API endpoints in frontend components if needed.

📚 Available Scripts

npm start → Run the app in development mode

npm test → Run tests

npm run build → Build for production

npm run eject → Eject CRA config (not recommended)

📦 Dependencies
Main Dependencies

React
 ^19.1.1

React DOM
 ^19.1.1

React Router DOM
 ^7.8.2

Axios
 ^1.11.0

Bootstrap
 ^5.3.7

React Scripts (CRA)
 5.0.1

Web Vitals
 ^2.1.4

Testing Dependencies

@testing-library/react
 ^16.3.0

@testing-library/jest-dom
 ^6.8.0

@testing-library/user-event
 ^13.5.0

@testing-library/dom
 ^10.4.1


