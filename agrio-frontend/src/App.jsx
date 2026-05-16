import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import Login from "./pages/Login";
import Navbar from "./pages/Navbar";
import Footer from "./pages/Footer";
import Dashboard from "./pages/Dashboard";

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

        {/* Home Page */}

        <Route
          path="/"
          element={<Home />}
        />

        {/* Extra Home Route */}

        <Route
          path="/home"
          element={<Home />}
        />

        {/* Login Page */}

        <Route
          path="/login"
          element={<Login />}
        />

      </Routes>

    </BrowserRouter>

  );
}

export default App;