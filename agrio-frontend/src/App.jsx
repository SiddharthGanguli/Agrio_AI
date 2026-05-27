import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import Login from "./pages/Login";
import Navbar from "./pages/Navbar";
import Footer from "./pages/Footer";
import Dashboard from "./pages/Dashboard";
import About from "./pages/About";

/* NEW IMPORT */
import CropRecommendation from "./pages/CropRecommendation";


function Home() {

  return (

    <>
      <Navbar />
      <Dashboard />
      <Footer />
    </>

  );
}

function App() {

  return (

    <BrowserRouter>

      <Routes>

        {/* ================= HOME PAGE ================= */}

        <Route
          path="/"
          element={<Home />}
        />

        <Route
          path="/home"
          element={<Home />}
        />


        {/* ================= LOGIN PAGE ================= */}

        <Route
          path="/login"
          element={<Login />}
        />


        {/* ================= ABOUT PAGE ================= */}

        <Route
          path="/about"
          element={
            <>
              <Navbar />
              <About />
              <Footer />
            </>
          }
        />


        {/* ================= CROP RECOMMENDATION PAGE ================= */}

        <Route
          path="/crop-recommendation"
          element={
            <>
              <Navbar />
              <CropRecommendation />
              <Footer />
            </>
          }
        />

      </Routes>

    </BrowserRouter>

  );
}

export default App;