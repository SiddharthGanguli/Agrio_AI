import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";

import Login from "./pages/Login";
import Navbar from "./pages/Navbar";

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

      </Routes>
    </BrowserRouter>
  );
}

export default App;