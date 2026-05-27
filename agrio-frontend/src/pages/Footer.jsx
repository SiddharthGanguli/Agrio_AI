import React from "react";

import { useNavigate, useLocation } from "react-router-dom";

import "./../styles/Footer.css";

/* ── All links — edit here only ── */

const FOOTER_LINKS = [

  {
    heading: "PRODUCT",

    links: [

      {
        label: "Crop Recommendation",
        id: "features",
      },

      {
        label: "Yield Prediction",
        id: "features",
      },

      {
        label: "Disease Detection",
        id: "features",
      },

    ],
  },

  {
    heading: "ABOUT",

    links: [

      {
        label: "About Us",
        id: "about",
      },

      {
        label: "Blog",
        id: "home",
      },

      {
        label: "Contact",
        id: "chat",
      },

    ],
  },

  {
    heading: "LEGAL",

    links: [

      {
        label: "Privacy Policy",
        id: "home",
      },

      {
        label: "Terms of Service",
        id: "home",
      },

    ],
  },

];

function Footer() {

  const navigate = useNavigate();

  const location = useLocation();

  const handleNavigation = (id) => {

    // ABOUT PAGE

    if (id === "about") {

      navigate("/about");

      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });

      return;
    }

    // HOME PAGE

    if (id === "home") {

      navigate("/");

      window.scrollTo({
        top: 0,
        behavior: "smooth",
      });

      return;
    }

    // SCROLL TO SECTION

    if (location.pathname === "/") {

      const section =
        document.getElementById(id);

      if (section) {

        section.scrollIntoView({
          behavior: "smooth",
        });
      }

    } else {

      navigate("/");

      setTimeout(() => {

        const section =
          document.getElementById(id);

        if (section) {

          section.scrollIntoView({
            behavior: "smooth",
          });
        }

      }, 300);
    }
  };

  return (

    <footer className="footer">

      <div className="footer-top">

        {/* Brand */}

        <div className="footer-brand">

          <h2>

            Agrio
            <span className="footer-ai">
              .ai
            </span>

          </h2>

          <p>

            Empowering farmers with intelligent,
            data-driven insights for every season.

          </p>

          <div className="footer-line"></div>

        </div>

        {/* Footer Links */}

        <div className="footer-links">

          {
            FOOTER_LINKS.map((col) => (

              <div
                className="footer-column"
                key={col.heading}
              >

                <h3>{col.heading}</h3>

                {
                  col.links.map((l) => (

                    <button
                      key={l.label}
                      className="footer-link-btn"
                      onClick={() =>
                        handleNavigation(l.id)
                      }
                    >

                      {l.label}

                    </button>

                  ))
                }

              </div>

            ))
          }

        </div>

      </div>

      {/* Bottom */}

      <div className="footer-bottom">

        <p>

          © {new Date().getFullYear()}
          {" "}
          Agrio.ai — All rights reserved.

        </p>

        <p>

          Crafted with care for the farming community 🌱

        </p>

      </div>

    </footer>
  );
}

export default Footer;