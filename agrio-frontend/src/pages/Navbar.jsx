import { useState } from "react";
import "../styles/Navbar.css";
export default function Navbar() {
  const [active, setActive] = useState("home");

  const links = [
    { id: "home", label: "Home" },
    { id: "about", label: "About" },
    { id: "weather", label: "Weather" },
  ];

  return (
    <div className="navbar-wrap">
      <nav className="navbar">

        {/* Logo */}
        <div className="logo">
          <div className="logo-icon">
            <svg
              width="24"
              height="24"
              viewBox="0 0 24 24"
              fill="none"
            >
              <path
                d="M6 20 C6 20 8 12 16 8 C18 7 21 7 21 7 C21 7 21 10 20 12 C18 16 14 19 9 20 Z"
                fill="white"
              />
              <path
                d="M6 20 C7 16 10 13 14 11"
                stroke="white"
                strokeWidth="1.4"
                strokeLinecap="round"
                fill="none"
                opacity="0.6"
              />
            </svg>
          </div>

          <span className="logo-text">
            Agrio<span className="logo-ai">.ai</span>
          </span>
        </div>

        {/* Nav Links */}
        <ul className="nav-links">
          {links.map((link) => (
            <li key={link.id}>
              <button
                onClick={() => setActive(link.id)}
                className={`nav-btn ${
                  active === link.id ? "active" : ""
                }`}
              >
                {link.label}
              </button>
            </li>
          ))}
        </ul>

        {/* Auth Buttons */}
        <div className="auth-group">
          <button className="btn-signin">Sign In</button>
          <button className="btn-signup">Sign Up</button>
        </div>

      </nav>
    </div>
  );
}