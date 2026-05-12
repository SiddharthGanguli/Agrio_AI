// Footer.jsx

import React from "react";

import "./../styles/Footer.css";

function Footer() {

  return (

    <footer className="footer">

      <div className="footer-top">

        {/* Brand Section */}

        <div className="footer-brand">

          <h2>
            Agrio.ai
          </h2>

          <p>
            Empowering farmers with
            intelligent, data-driven insights
            for every season.
          </p>

          <div className="footer-line"></div>

        </div>

        {/* Links */}

        <div className="footer-links">

          {/* Product */}

          <div className="footer-column">

            <h3>
              PRODUCT
            </h3>

            <a href="">
              Crop Recommendation
            </a>

            <a href="">
              Yield Prediction
            </a>

            <a href="">
              Disease Detection
            </a>

      

          </div>

          {/* About */}

          <div className="footer-column">

            <h3>
              ABOUT
            </h3>

            <a href="">
              About Us
            </a>

            <a href="">
              Blog
            </a>

      

            <a href="">
              Contact
            </a>

          </div>

          {/* Legal */}

          <div className="footer-column">

            <h3>
              LEGAL
            </h3>

            <a href="">
              Privacy Policy
            </a>

            <a href="">
              Terms of Service
            </a>

          </div>

        </div>

      </div>

      {/* Bottom */}

      <div className="footer-bottom">

        <p>
          © 2026 Agrio.ai — All rights reserved.
        </p>

        <p>
          Crafted with care for the farming community 🌱
        </p>

      </div>

    </footer>

  );
}

export default Footer;