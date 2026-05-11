import { useEffect, useState } from "react";

import {
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  onAuthStateChanged,
} from "firebase/auth";

import { auth } from "../firebase";

import "../styles/login.css";

function Login() {
  const [isLogin, setIsLogin] = useState(true);

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  // Register User
  const handleRegister = async () => {
    try {
      const user = await createUserWithEmailAndPassword(
        auth,
        email,
        password
      );

      console.log("User Created:", user);

      alert("Account Created Successfully");

    } catch (error) {
      alert(error.message);
    }
  };

  // Login User
  const handleLogin = async () => {
    try {
      const user = await signInWithEmailAndPassword(
        auth,
        email,
        password
      );

      console.log("Login Success:", user);

      alert("Login Successful");

    } catch (error) {
      alert(error.message);
    }
  };

  // Store User Session
  useEffect(() => {

    const unsubscribe = onAuthStateChanged(
      auth,
      (user) => {

        if (user) {

          console.log("User Logged In:", user);

          localStorage.setItem(
            "user",
            JSON.stringify(user)
          );

        } else {

          localStorage.removeItem("user");
        }
      }
    );

    return () => unsubscribe();

  }, []);

  return (
    <div className="container">

      <div className="auth-box">

        <h1>AGRIO AI</h1>

        <p>
          {isLogin
            ? "Login to continue"
            : "Create your account"}
        </p>

        {!isLogin && (
          <input
            type="text"
            placeholder="Full Name"
          />
        )}

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
          {isLogin
            ? "Login"
            : "Create Account"}
        </button>

        <div className="switch">

          {isLogin ? (
            <>
              <span>New User?</span>

              <button
                className="link-btn"
                onClick={() =>
                  setIsLogin(false)
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
                  setIsLogin(true)
                }
              >
                Login
              </button>
            </>
          )}

        </div>

      </div>

    </div>
  );
}

export default Login;