import "../styles/About.css";

import AgrioImage from "../assets/Agrio.jpg";

function About() {

  return (


    <div className="about-page">

      {/* ========================= */}
      {/* SECTION 1 */}
      {/* ========================= */}

      <section className="about-section">

        {/* Left Side */}

        <div className="about-left">

          <p className="about-tag">
            ABOUT AGRIO AI
          </p>

          <h1 className="about-heading">
            We bring <span>ML</span>
            <br />
            to the
            <br />
            field.
          </h1>

          <p className="about-description">

            A three-person team building precision agriculture
            intelligence. One chatbot that understands your
            farm, classifies your problem, and routes it to the
            right ML model — automatically.

          </p>

          <div className="about-cards">

            <div className="info-card">
              <h2>3</h2>
              <p>ML models</p>
            </div>

            <div className="info-card">
              <h2>1</h2>
              <p>unified chatbot interface</p>
            </div>

            <div className="info-card">
              <h2>∞</h2>
              <p>farm queries, one answer</p>
            </div>

          </div>

        </div>

        {/* Right Side */}

        <div className="about-right">

          <img
            src={AgrioImage}
            alt="Farm"
          />

          <div className="floating-card soil-card">

            <p>soil reading</p>

            <h3>
              34 23 45
            </h3>

            <span>
              N &nbsp; P &nbsp; K
            </span>

          </div>

          <div className="floating-card disease-card">

            <p>disease detected</p>

            <h4>
              Leaf blight
            </h4>

          </div>

          <div className="floating-card output-card">

            <p>
              ✓ model output
            </p>

            <h4>
              "Grow rice — 94%
              <br />
              match for your
              <br />
              conditions"
            </h4>

          </div>

        </div>

      </section>

      {/* ========================= */}
      {/* SECTION 2 */}
      {/* ========================= */}

      <section className="workflow-section">

        <p className="workflow-tag">
          WHAT WE BUILD
        </p>

        <h2 className="workflow-title">
          One chatbot. Three models.
        </h2>

        <p className="workflow-desc">

          You describe your situation in plain language —
          soil readings, a photo of a diseased leaf,
          or a question about yield. The chatbot classifies
          your intent and silently routes it to the correct
          model. You get a direct answer.

        </p>

        {/* FLOW */}

        <div className="workflow-flow">

          <div className="flow-box">

            <h3>User Query</h3>

            <p>
              text prompt or image upload
            </p>

          </div>

          <div className="flow-line"></div>

          <div className="flow-box active-box">

            <h3>AI Chatbot</h3>

            <p>
              intent classifier → routes to model
            </p>

          </div>

          {/* MODEL CARDS */}

          <div className="model-row">

            <div className="model-card">

              <h3>
                Crop Recommendation
              </h3>

              <span>
                soil params
              </span>

              <div className="result-box">

                "Grow rice — optimal match 94%"

              </div>

            </div>

            <div className="model-card">

              <h3>
                Yield Prediction
              </h3>

              <span>
                season + region
              </span>

              <div className="result-box">

                "Expected yield: 3.2 t/ha"

              </div>

            </div>

            <div className="model-card">

              <h3>
                Disease Detection
              </h3>

              <span>
                plant image
              </span>

              <div className="result-box">

                "Leaf blight detected"

              </div>

            </div>

          </div>

          <div className="flow-line"></div>

          <div className="flow-box response-box">

            <h3>
              Response to User
            </h3>

            <p>
              prediction + explanation in plain language
            </p>

          </div>

        </div>

        {/* EXAMPLES */}

        <div className="example-row">

          <div className="example-card">

            <p>
              "My soil has N=34, P=23, K=45,
              pH=6.2. What crop should I grow?"
            </p>

            <span>
              → Crop Recommendation
            </span>

          </div>

          <div className="example-card">

            <p>
              "What yield can I expect for maize
              in Kharif season?"
            </p>

            <span>
              → Yield Prediction
            </span>

          </div>

          <div className="example-card">

            <p>
              "My tomato leaves have yellow spots."
            </p>

            <span>
              → Disease Detection
            </span>

          </div>

        </div>

      </section>

      {/* ========================= */}
{/* SECTION 3 */}
{/* ========================= */}

<section className="models-section">

  <p className="models-tag">
    THE MODELS
  </p>

  <h2 className="models-title">
    Three models, one platform
  </h2>

  {/* MODEL 1 */}

  <div className="model-item">

    <div className="model-number">
      01
    </div>

    <div className="model-icon">
      🌱
    </div>

    <div className="model-content">

      <h3>
        Crop Recommendation
      </h3>

      <p>

        Given soil parameters (N, P, K,
        temperature, humidity, pH, rainfall),
        the model classifies and recommends
        the most suitable crop to grow.

      </p>

      <span>
        ● Input: N, P, K, temp, humidity, pH, rainfall
      </span>

    </div>

  </div>

  {/* MODEL 2 */}

  <div className="model-item">

    <div className="model-number">
      02
    </div>

    <div className="model-icon">
      📈
    </div>

    <div className="model-content">

      <h3>
        Yield Prediction
      </h3>

      <p>

        Predicts the expected crop yield
        based on historical data, season,
        region, and current soil and weather
        conditions.

      </p>

      <span>
        ● Input: Season, region, soil conditions
      </span>

    </div>

  </div>

  {/* MODEL 3 */}

  <div className="model-item">

    <div className="model-number">
      03
    </div>

    <div className="model-icon">
      🔬
    </div>

    <div className="model-content">

      <h3>
        Disease Detection
      </h3>

      <p>

        User uploads a photo of an affected
        plant. The model identifies the
        disease, its severity, and suggests
        treatment steps.

      </p>

      <span>
        ● Input: Plant image upload
      </span>

    </div>

  </div>

</section>
{/* ========================= */}
{/* SECTION 4 */}
{/* ========================= */}

<section className="team-section">

  <p className="team-tag">
    WHO WE ARE
  </p>

  <h2 className="team-title">
    Three people, one goal
  </h2>

  <div className="team-grid">

    {/* MEMBER 1 */}

    <div className="team-card">

      <div className="team-image">
        AD
      </div>

      <h3>
        Amara Diallo
      </h3>

      <span>
        ML ENGINEER
      </span>

    </div>

    {/* MEMBER 2 */}

    <div className="team-card">

      <div className="team-image">
        LF
      </div>

      <h3>
        Lucas Ferreira
      </h3>

      <span>
        BACKEND & DATA
      </span>

    </div>

    {/* MEMBER 3 */}

    <div className="team-card">

      <div className="team-image">
        YP
      </div>

      <h3>
        Yuna Park
      </h3>

      <span>
        PRODUCT & FRONTEND
      </span>

    </div>

  </div>

</section>

    </div>

  );
}

export default About;
