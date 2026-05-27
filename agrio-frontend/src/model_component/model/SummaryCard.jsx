import React from "react";

function SummaryCard({ summary }) {

  return (

    <div className="summary-card">

      <h3 className="card-title">
        Summary
      </h3>

      <p className="summary-text">
        {summary}
      </p>

    </div>

  );
}

export default SummaryCard;