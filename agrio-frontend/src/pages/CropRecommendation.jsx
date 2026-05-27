import React, { useState } from "react";

import "../styles/CropRecommendation.css";

/* ================= COMPONENTS ================= */

import MyInput from "../model_component/model/MyInput.jsx";
import EmptyPrediction from "../model_component/model/EmptyPrediction.jsx";
import PredictionCard from "../model_component/model/PredictionCard.jsx";
import SummaryCard from "../model_component/model/SummaryCard.jsx";
import ValuesCard from "../model_component/model/ValuesCard.jsx";

function CropRecommendation() {

  /* ================= FORM STATE ================= */

  const [formData, setFormData] = useState({
    nitrogen: "",
    phosphorus: "",
    potassium: "",
    temperature: "",
    humidity: "",
    ph: "",
    rainfall: "",
  });

  /* ================= PREDICTION STATE ================= */

  const [prediction, setPrediction] = useState(null);

  /* ================= HANDLE INPUT ================= */

  const handleChange = (e) => {

    const { name, value } = e.target;

    setFormData({
      ...formData,
      [name]: value,
    });

  };

  /* ================= HANDLE PREDICT ================= */

  const handlePredict = () => {

    /* TEMPORARY DUMMY RESPONSE */

    setPrediction({
      crop: "Rice",
      confidence: 87,
      summary:
        `Based on your soil conditions and environmental factors,
        the model recommends growing Rice with high confidence.`,
    });

  };

  /* ================= HANDLE RESET ================= */

  const handleReset = () => {

    setFormData({
      nitrogen: "",
      phosphorus: "",
      potassium: "",
      temperature: "",
      humidity: "",
      ph: "",
      rainfall: "",
    });

    setPrediction(null);

  };

  return (

    <div className="crop-page">

      {/* ================= HEADER SECTION ================= */}

      <div className="crop-header-section">

        <div className="model-title-wrapper">

          <div className="model-icon-box">
            🌿
          </div>

          <div>

            <h1 className="model-main-title">
              Crop Recommendation
            </h1>

            <p className="model-number">
              MODEL 01
            </p>

          </div>

        </div>

        <p className="model-description">
          Enter your soil parameters and environmental conditions
          to get a recommendation for the most suitable crop to grow.
        </p>

      </div>

      {/* ================= MAIN SECTION ================= */}

      <div className="crop-main-section">

        {/* ================= LEFT FORM SECTION ================= */}

        <div className="crop-form-section">

          <div className="crop-form-card">

            <h2 className="section-title">
              Input Parameters
            </h2>

            {/* ================= INPUTS ================= */}

            <div className="input-group">

              <MyInput
                label="Nitrogen (N) (kg/ha)"
                name="nitrogen"
                value={formData.nitrogen}
                onChange={handleChange}
                placeholder="e.g., 43"
              />

              <MyInput
                label="Phosphorus (P) (kg/ha)"
                name="phosphorus"
                value={formData.phosphorus}
                onChange={handleChange}
                placeholder="e.g., 34"
              />

              <MyInput
                label="Potassium (K) (kg/ha)"
                name="potassium"
                value={formData.potassium}
                onChange={handleChange}
                placeholder="e.g., 4"
              />

              <MyInput
                label="Temperature (°C)"
                name="temperature"
                value={formData.temperature}
                onChange={handleChange}
                placeholder="e.g., 43"
              />

              <MyInput
                label="Humidity (%)"
                name="humidity"
                value={formData.humidity}
                onChange={handleChange}
                placeholder="e.g., 34"
              />

              <MyInput
                label="pH Level"
                name="ph"
                value={formData.ph}
                onChange={handleChange}
                placeholder="e.g., 7"
              />

              <MyInput
                label="Rainfall (mm)"
                name="rainfall"
                value={formData.rainfall}
                onChange={handleChange}
                placeholder="e.g., 202"
              />

            </div>

            {/* ================= BUTTONS ================= */}

            <div className="button-group">

              <button
                className="predict-btn"
                onClick={handlePredict}
              >
                Get Recommendation
              </button>

              <button
                className="reset-btn"
                onClick={handleReset}
              >
                Reset
              </button>

            </div>

          </div>

        </div>

        {/* ================= RIGHT RESULT SECTION ================= */}

        <div className="crop-result-section">

          <h2 className="section-title">
            Prediction Result
          </h2>

          <div className="result-wrapper">

            {/* ================= EMPTY STATE ================= */}

            {!prediction && (
              <EmptyPrediction />
            )}

            {/* ================= RESULT STATE ================= */}

            {prediction && (

              <div className="result-cards-wrapper">

                <PredictionCard
                  crop={prediction.crop}
                  confidence={prediction.confidence}
                />

                <SummaryCard
                  summary={prediction.summary}
                />

                <ValuesCard
                  formData={formData}
                />

              </div>

            )}

          </div>

        </div>

      </div>

    </div>

  );
}

export default CropRecommendation;