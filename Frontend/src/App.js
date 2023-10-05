import Home from "./Component/Home";
import Extra from "./Component/Extra";
import About from "./Component/About";
import { onAuthStateChanged } from "firebase/auth";
import React,{useEffect,useState} from "react";
import {auth} from './firebase';

function App() {
  const [authUser, setAuthUser] = useState(null);
  useEffect(()=>{
      const listen = onAuthStateChanged(auth,(user)=>{
          if (user){
              setAuthUser(user)
          }else{
              setAuthUser(null);
          }
      })
  },[])
  return (
    <div>
      <Home/> 
      <About/>   
    </div>
  );
}

export default App;
