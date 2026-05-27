import React from "react";

function MyInput({
  label,
  name,
  value,
  onChange,
  placeholder,
}) {

  return (

    <div className="input-wrapper">

      <label className="input-label">
        {label}
      </label>

      <input
        type="number"
        name={name}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        className="input-field"
      />

    </div>

  );
}

export default MyInput;