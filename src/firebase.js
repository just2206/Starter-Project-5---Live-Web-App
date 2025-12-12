// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCuKOehQDZarDmTDjJVH-7ZoVam7hKzYjU",
  authDomain: "boggle-1b38d.firebaseapp.com",
  projectId: "boggle-1b38d",
  storageBucket: "boggle-1b38d.firebasestorage.app",
  messagingSenderId: "416566470936",
  appId: "1:416566470936:web:aed97ca938f6bf0f53966d",
  measurementId: "G-ZM6KG8YM3P"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);