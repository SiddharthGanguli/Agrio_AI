import React from "react";

function PredictionCard({
  crop,
  confidence,
}) {

  return (

    <div className="prediction-card">

      <p className="prediction-label">
        RECOMMENDED CROP
      </p>

      <h1 className="prediction-crop">
        {crop}
      </h1>

      {/* ================= CONFIDENCE BAR ================= */}

      <div className="confidence-wrapper">

        <div className="confidence-bar-bg">

          <div
            className="confidence-bar-fill"
            style={{
              width: `${confidence}%`,
            }}
          ></div>

        </div>

        <span className="confidence-percent">
          {confidence}%
        </span>

      </div>

      <p className="confidence-text">
        Confidence Level
      </p>

    </div>

  );
}

export default PredictionCard;