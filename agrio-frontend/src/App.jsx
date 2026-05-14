// App.jsx

import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/login";

import Dashboard from "./pages/Dashboard";

import CropRecommendation from "./pages/CropRecommendation";

import CropYieldPrediction from "./pages/CropYieldPrediction";

import CropDiseasePrediction from "./pages/CropDiseasePrediction";

function App() {

  return (

    <BrowserRouter>

      <Routes>

        <Route
          path="/"
          element={<Login />}
        />

        <Route
          path="/dashboard"
          element={<Dashboard />}
        />

        <Route
          path="/crop-recommendation"
          element={<CropRecommendation />}
        />

        <Route
          path="/crop-yield"
          element={<CropYieldPrediction />}
        />

        <Route
          path="/crop-disease"
          element={<CropDiseasePrediction />}
        />

      </Routes>

    </BrowserRouter>

  );
}

export default App;