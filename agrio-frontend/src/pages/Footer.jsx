import React from "react";
import "./../styles/Footer.css";

/* ── All links — edit here only ── */
const FOOTER_LINKS = [
  {
    heading: "PRODUCT",
    links: [
      { label: "Crop Recommendation", href: "#features" },
      { label: "Yield Prediction",    href: "#features" },
      { label: "Disease Detection",   href: "#features" },
    ],
  },
  {
    heading: "ABOUT",
    links: [
      { label: "About Us", href: "#about"   },
      { label: "Blog",     href: "#"        },
      { label: "Contact",  href: "#"        },
    ],
  },
  {
    heading: "LEGAL",
    links: [
      { label: "Privacy Policy",   href: "#" },
      { label: "Terms of Service", href: "#" },
    ],
  },
];

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-top">

        {/* Brand */}
        <div className="footer-brand">
          <h2>Agrio<span className="footer-ai">.ai</span></h2>
          <p>Empowering farmers with intelligent, data-driven insights for every season.</p>
          <div className="footer-line"></div>
        </div>

        {/* Links — rendered from data */}
        <div className="footer-links">
          {FOOTER_LINKS.map((col) => (
            <div className="footer-column" key={col.heading}>
              <h3>{col.heading}</h3>
              {col.links.map((l) => (
                <a href={l.href} key={l.label}>{l.label}</a>
              ))}
            </div>
          ))}
        </div>

      </div>

      {/* Bottom */}
      <div className="footer-bottom">
        <p>© {new Date().getFullYear()} Agrio.ai — All rights reserved.</p>
        <p>Crafted with care for the farming community 🌱</p>
      </div>
    </footer>
  );
}

export default Footer;