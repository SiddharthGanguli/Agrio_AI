import "../styles/Dashboard.css";

import AgrioImage from "../assets/Agrio.jpg";

/* ── All content — edit here only ── */

const FEATURES = [

  {
    id: 1,
    icon: "🌱",
    title: "Crop Recommendation Model",
    desc: "Get the best crop for your soil, climate, and season.",
  },

  {
    id: 2,
    icon: "📈",
    title: "Crop Yield Prediction Model",
    desc: "Forecast harvest output and plan resources with ease.",
  },

  {
    id: 3,
    icon: "🔬",
    title: "Crop Disease Detection Model",
    desc: "Upload a leaf image and detect disease in seconds.",
  },

];

const CHAT_BUBBLES = [

  {
    from: "user",
    text: "Which crop suits black soil in monsoon?",
  },

  {
    from: "ai",
    text: "Soybean is ideal for your conditions 🌿",
  },

  {
    from: "user",
    text: "What yield can I expect for 2 acres?",
  },

  {
    from: "ai",
    text: "Approximately 3.4 tonnes based on current data 📊",
  },

];

/* ── Hero ── */

function Hero() {

  return (

    <section className="hero" id="home">

      <div className="hero-content">

        {/* Left Side */}

        <div className="hero-left">

          <span className="badge">
            🌾 AI-Powered Agriculture
          </span>

          <h1>

            Farm Smarter.

            <br />

            <span className="accent">
              Harvest Better.
            </span>

          </h1>

          <p className="hero-sub">

            Three intelligent models to recommend crops,
            predict yield, and detect disease —
            all in one platform.

          </p>

          <div className="hero-btns">

            <a
              href="#features"
              className="btn-primary"
            >
              Explore Models
            </a>

            <a
              href="#chat"
              className="btn-outline"
            >
              Chat with AI
            </a>

          </div>

        </div>

        {/* Right Side Image */}

        <div className="hero-right">

          <img
            src={AgrioImage}
            alt="Agriculture"
          />

        </div>

      </div>

    </section>
  );
}

/* ── Feature Cards ── */

function Features() {

  return (

    <section
      className="features"
      id="features"
    >

      <p className="eyebrow">
        Our Models
      </p>

      <h2>
        What Agrio AI Can Do
      </h2>

      <div className="cards">

        {
          FEATURES.map((f) => (

            <div
              className="card"
              key={f.id}
            >

              <span className="card-icon">
                {f.icon}
              </span>

              <h3>
                {f.title}
              </h3>

              <p>
                {f.desc}
              </p>

            </div>

          ))
        }

      </div>

    </section>
  );
}

/* ── Chat ── */

function Chat() {

  return (

    <section
      className="chat"
      id="chat"
    >

      <p className="eyebrow">
        AI Assistant
      </p>

      <h2>
        Ask Agrio AI Anything
      </h2>

      <p className="chat-sub">

        Get instant answers on crops,
        soil, and diseases — 24/7.

      </p>

      <div className="chat-window">

        <div className="chat-bar">
          💬 Agrio AI Chat
        </div>

        <div className="chat-msgs">

          {
            CHAT_BUBBLES.map((b, i) => (

              <div
                key={i}
                className={`bubble bubble-${b.from}`}
              >

                {b.text}

              </div>

            ))
          }

        </div>

        <div className="chat-footer">

          <button className="btn-primary chat-btn">

            Chat Now →

          </button>

        </div>

      </div>

    </section>
  );
}

/* ── Dashboard ── */

export default function Dashboard() {

  return (

    <div className="dashboard">

      <Hero />

      <Features />

      <Chat />

    </div>
  );
}