import React from "react";
import { useNavigate, useLocation } from "react-router-dom";
import './Dashboard.css';

function Dashboard() {
  const navigate = useNavigate();
  const location = useLocation();
  const user = location.state?.user;

  if (!user) {
    navigate("/");
    return null;
  }

  const handleLogout = () => {
    navigate("/");
  };

  return (
    <div className="dashboard-container">
      <div className="glass-card text-center p-5">
        <h1 className="fw-bold mb-4">🌟 Welcome, {user.name}</h1>
        <p className="lead mb-4">
          You have successfully logged in!
        </p>

        <div className="info-card p-4 mb-4">
          <h5>User Information</h5>
          <p>
            <b>Name:</b> {user.name} <br />
            <b>Confidence:</b> {(user.confidence * 100).toFixed(2)}% <br />
            <b>Status:</b> Logged In
          </p>
        </div>

        <button className="btn btn-custom btn-lg fw-bold" onClick={handleLogout}>
          🔙 Logout
        </button>
      </div>
    </div>
  );
}

export default Dashboard;


// import React from "react";
// import { useNavigate } from "react-router-dom";
// import 'bootstrap/dist/css/bootstrap.min.css';
// import './Dashboard.css'; // optional for extra styling

// function Dashboard() {
//   const navigate = useNavigate();

//   const handleLogout = () => {
//     navigate("/"); // go back to recognition/login page
//   };

//   return (
//     <div className="d-flex justify-content-center align-items-center min-vh-100" style={{ backgroundColor: "#f0f4ff" }}>
//       <div className="glass-card text-center p-5" style={{ maxWidth: "500px", borderRadius: "15px" }}>
//         <h1 className="fw-bold mb-4">🌟 Welcome to Your Dashboard</h1>
//         <p className="lead mb-4">
//           You have successfully logged in! Enjoy your personalized dashboard experience.
//         </p>

//         <div className="info-card bg-light p-3 mb-4" style={{ borderRadius: "10px" }}>
//           <h5>User Information</h5>
//           <p>
//             <b>Name:</b> John Doe <br />
//             <b>Role:</b> User <br />
//             <b>Status:</b> Logged In
//           </p>
//         </div>

//         <button className="btn btn-primary btn-lg fw-bold" onClick={handleLogout}>
//           🔙 Logout
//         </button>
//       </div>
//     </div>
//   );
// }

// export default Dashboard;
