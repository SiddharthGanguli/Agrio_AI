import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import Login from "./pages/Login";
import Navbar from "./pages/Navbar";
import Footer from "./pages/Footer";

function App() {
  return (
    <BrowserRouter>
      <Routes>

        <Route
          path="/"
          element={<Login />}
        />

        <Route
          path="/navbar"
          element={<Navbar />}
        />

      <Route
          path="/footer"
          element={<Footer />}
        />


      </Routes>
    </BrowserRouter>
  );
}

export default App;