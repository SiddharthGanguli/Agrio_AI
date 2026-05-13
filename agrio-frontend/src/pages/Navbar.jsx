import { useState, useEffect } from "react";
import "../styles/Navbar.css";

const links = [
  { id: "home",     label: "Home",     href: "#home"     },
  { id: "features", label: "Models",   href: "#features" },
  { id: "chat",     label: "Chat",     href: "#chat"     },
  { id: "about",    label: "About",    href: "#about"    },
  { id: "weather",  label: "Weather",  href: "#weather"  },
];

export default function Navbar() {
  const [active, setActive] = useState("home");
  const [scrolled, setScrolled] = useState(false);

  // Add background blur when user scrolls down
  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 40);
    window.addEventListener("scroll", onScroll);
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  return (
    <div className={`navbar-wrap ${scrolled ? "scrolled" : ""}`}>
      <nav className="navbar">

        {/* Logo */}
        <div className="logo">
          <div className="logo-icon">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
              <path
                d="M6 20 C6 20 8 12 16 8 C18 7 21 7 21 7 C21 7 21 10 20 12 C18 16 14 19 9 20 Z"
                fill="white"
              />
              <path
                d="M6 20 C7 16 10 13 14 11"
                stroke="white" strokeWidth="1.4"
                strokeLinecap="round" fill="none" opacity="0.6"
              />
            </svg>
          </div>
          <span className="logo-text">
            Agrio<span className="logo-ai">.ai</span>
          </span>
        </div>

        {/* Nav Links — now scroll to sections */}
        <ul className="nav-links">
          {links.map((link) => (
            <li key={link.id}>
              <a
                href={link.href}
                onClick={() => setActive(link.id)}
                className={`nav-btn ${active === link.id ? "active" : ""}`}
              >
                {link.label}
              </a>
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