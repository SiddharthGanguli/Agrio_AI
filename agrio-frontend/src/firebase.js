import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyDLfijYnSGrmk0_TQSagAY8OF_iX7lxtVc",
  authDomain: "agrio-ai.firebaseapp.com",
  projectId: "agrio-ai",
  storageBucket: "agrio-ai.firebasestorage.app",
  messagingSenderId: "232552971574",
  appId: "1:232552971574:web:d8549a92924fab70e18797",
  measurementId: "G-87CN2XQ1E2"
};
const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);