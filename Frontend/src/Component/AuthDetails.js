import { onAuthStateChanged } from "firebase/auth";
import React,{useEffect,useState} from "react";
import {auth} from '../firebase';
import Extra from "./Extra";
import Home from "./Home";

const AuthDetails =()=>{
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
    return(
        <div>{ authUser ? <Extra/> : <p><Home/></p>}</div>
    )
}

export default AuthDetails