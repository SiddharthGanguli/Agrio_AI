import { useEffect, useState } from "react";

import {
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  onAuthStateChanged,
} from "firebase/auth";

import {
  useNavigate,
  useLocation
} from "react-router-dom";

import { auth } from "../firebase";

import "../styles/login.css";

function Login() {

  const navigate = useNavigate();

  const location = useLocation();

  const [isLogin, setIsLogin] = useState(true);

  const [name, setName] = useState("");

  const [email, setEmail] = useState("");

  const [password, setPassword] = useState("");

  // Detect URL mode

  useEffect(() => {

    if (location.search === "?mode=signup") {

      setIsLogin(false);

    } else {

      setIsLogin(true);

    }

  }, [location]);

  // Register User

  const handleRegister = async () => {

    try {

      if (!name.trim()) {

        alert("Please enter your full name");

        return;

      }

      const userCredential =
        await createUserWithEmailAndPassword(
          auth,
          email,
          password
        );

      const user = userCredential.user;

      // Save user data properly

      localStorage.setItem(
        "user",
        JSON.stringify({

          uid: user.uid,

          email: user.email,

          name: name.trim(),

        })
      );

      console.log(
        JSON.parse(localStorage.getItem("user"))
      );

      alert("Account Created Successfully");

      // Go to Login Page

      navigate("/login");

    } catch (error) {

      alert(error.message);

    }
  };

  // Login User

  const handleLogin = async () => {

    try {

      const userCredential =
        await signInWithEmailAndPassword(
          auth,
          email,
          password
        );

      const user = userCredential.user;

      // Get old stored data

      const storedUser = JSON.parse(
        localStorage.getItem("user")
      );

      localStorage.setItem(
        "user",
        JSON.stringify({

          uid: user.uid,

          email: user.email,

          name: storedUser?.name || "User",

        })
      );

      alert("Login Successful");

      navigate("/");

    } catch (error) {

      alert(error.message);

    }
  };

  // Auth Listener

  useEffect(() => {

    const unsubscribe =
      onAuthStateChanged(
        auth,
        (user) => {

          console.log("User:", user);

        }
      );

    return () => unsubscribe();

  }, []);

  return (

    <div className="container">

      <div className="auth-box">

        <h1>
          AGRIO AI
        </h1>

        <p>

          {
            isLogin
              ? "Login to continue"
              : "Create your account"
          }

        </p>

        {

          !isLogin && (

            <input
              type="text"
              placeholder="Full Name"
              value={name}
              onChange={(e) =>
                setName(e.target.value)
              }
            />

          )

        }

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) =>
            setEmail(e.target.value)
          }
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) =>
            setPassword(e.target.value)
          }
        />

        <button
          onClick={
            isLogin
              ? handleLogin
              : handleRegister
          }
        >

          {

            isLogin
              ? "Login"
              : "Create Account"

          }

        </button>

        <div className="switch">

          {

            isLogin ? (

              <>

                <span>
                  New User?
                </span>

                <button
                  className="link-btn"
                  onClick={() =>
                    navigate("/login?mode=signup")
                  }
                >

                  Create Account

                </button>

              </>

            ) : (

              <>

                <span>
                  Already have an account?
                </span>

                <button
                  className="link-btn"
                  onClick={() =>
                    navigate("/login")
                  }
                >

                  Login

                </button>

              </>

            )

          }

        </div>

      </div>

    </div>
  );
}

export default Login;