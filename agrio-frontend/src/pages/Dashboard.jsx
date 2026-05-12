// Dashboard.jsx

import React from "react";

import { useNavigate } from "react-router-dom";

import "./../styles/Dashboard.css";

function Dashboard() {

  const navigate = useNavigate();

  return (

    <div className="dashboard-container">

      {/* Intro Section */}

      <div className="intro-section">

        <div className="intro-left">

          <h1>
            AI Powered Agriculture 
             <br />
  Platform
          </h1>

          <p>
            Get crop recommendations,
            yield predictions and crop
            disease detection using
            Machine Learning and AI.
          </p>

          <div className="intro-buttons">

            <button className="start-btn">
              Get Started
            </button>

            <button className="feature-btn">
              View Features
            </button>

          </div>

        </div>

        <div className="intro-right">

          <img
            src="https://images.unsplash.com/photo-1500937386664-56d1dfef3854?q=80&w=1200&auto=format&fit=crop"
            alt="Agriculture"
          />

        </div>

      </div>

      {/* ML Features */}

      <h1 className="feature-heading">
        Our ML Features
      </h1>

      {/* Your Existing Cards */}

      <div className="main-box">

        <div
          className="card"
          onClick={() =>
            navigate("/crop-recommendation")
          }
        >

          <h2>Crop Recommendation</h2>

          <p>
            Get the best crop based on soil
            nutrients and environmental
            conditions.
          </p>

          <button>
            Try Model
          </button>

        </div>

        <div
          className="card"
          onClick={() =>
            navigate("/crop-yield")
          }
        >

          <h2>Crop Yield Prediction</h2>

          <p>
            Predict crop production using
            historical and environmental
            data.
          </p>

          <button>
            Try Model
          </button>

        </div>

        <div
          className="card"
          onClick={() =>
            navigate("/crop-disease")
          }
        >

          <h2>Crop Disease Prediction</h2>

          <p>
            Detect crop diseases using
            image analysis and AI-based
            prediction.
          </p>

          <button>
            Try Model
          </button>

        </div>

      </div>

      {/* Ask Anything */}

      <div className="chat-box">

        <input
          type="text"
          placeholder="Ask anything..."
        />

        <button>
          Ask
        </button>

      </div>

    </div>
  );
}

export default Dashboard;