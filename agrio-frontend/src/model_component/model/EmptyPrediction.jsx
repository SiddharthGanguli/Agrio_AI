import React from "react";

function EmptyPrediction() {

  return (

    <div className="empty-result-card">

      <div className="empty-result-content">

        <div className="empty-icon">
          🌱
        </div>

        <p className="empty-text">
          Enter parameters and submit to see prediction
        </p>

      </div>

    </div>

  );
}

export default EmptyPrediction;