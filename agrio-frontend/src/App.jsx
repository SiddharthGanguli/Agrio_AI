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

        <Route
          path="/"
          element={<Login />}
        />

        <Route
          path="/home"
          element={<Home />}
        />

      </Routes>
    </BrowserRouter>
  );
}

export default App;