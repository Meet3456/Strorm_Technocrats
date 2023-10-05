// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDRt8giqRDcbUd8-5qn2YCmBHsAF0wQmbw",
  authDomain: "phishing-88c0a.firebaseapp.com",
  projectId: "phishing-88c0a",
  storageBucket: "phishing-88c0a.appspot.com",
  messagingSenderId: "854573462704",
  appId: "1:854573462704:web:2c98f683f5857a2b8bb775",
  measurementId: "G-RCQCQCSZ3E"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app)
const analytics = getAnalytics(app);