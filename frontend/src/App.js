import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Recognition from "./components/Recognition";
import Register from "./components/Register";
import Train from "./components/Train";
import Dashboard from "./components/Dashboard";





function App() {
  return (
    <Router>
      <div>
        {/* Navbar links */}
        <nav style={{ padding: "1rem", background: "#eee" }}>
          <Link to="/" style={{ marginRight: "1rem" }}>🏠 Recognition</Link>
          <Link to="/register" style={{ marginRight: "1rem" }}>➕ Register User</Link>
          <Link to="/train">➕ Train Model</Link>
         

        </nav>

        {/* Pages */}
        <Routes>
          <Route path="/" element={<Recognition />} />
          <Route path="/register" element={<Register />} />
          <Route path="/train" element={<Train />} />
         <Route path="/dashboard" element={<Dashboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
