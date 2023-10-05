import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { BrowserRouter, Route,Routes} from 'react-router-dom';
import Extra from './Component/Extra';
import About from './Component/About';
import Login from "./Component/Login";
import Register from "./Component/Register"
import Dashboard from './Component/Dashboard';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <BrowserRouter>
      <Routes>
      <Route path='/'element={<App/>}/>
      <Route path='/about'element={<About/>}/>
      <Route path='/home'element={<Extra/>}/>
      <Route path='/login'element={<Login/>}/>  
      <Route path='/register'element={<Register/>}/> 
      <Route path='/dashboard'element={<Dashboard/>}/>  
    </Routes>
    </BrowserRouter>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals

