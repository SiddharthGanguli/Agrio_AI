import React from "react";

function ValuesCard({ formData }) {

  return (

    <div className="values-card">

      <h3 className="card-title">
        Input Values
      </h3>

      <div className="values-grid">

        <div className="value-item">
          <span>Nitrogen</span>
          <strong>{formData.nitrogen}</strong>
        </div>

        <div className="value-item">
          <span>Phosphorus</span>
          <strong>{formData.phosphorus}</strong>
        </div>

        <div className="value-item">
          <span>Potassium</span>
          <strong>{formData.potassium}</strong>
        </div>

        <div className="value-item">
          <span>Temperature</span>
          <strong>{formData.temperature}°C</strong>
        </div>

        <div className="value-item">
          <span>Humidity</span>
          <strong>{formData.humidity}%</strong>
        </div>

        <div className="value-item">
          <span>pH Level</span>
          <strong>{formData.ph}</strong>
        </div>

        <div className="value-item">
          <span>Rainfall</span>
          <strong>{formData.rainfall}mm</strong>
        </div>

      </div>

    </div>

  );
}

export default ValuesCard;