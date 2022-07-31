import React from 'react';
import "./Navbar.css"
import {  Link } from "react-router-dom";

const Navbar= () =>{
  return (
    <header class="header">
      <div class="left">
        <a href="#">Animal Navbar</a>
      </div>
      <div class="mid">
        <ul class="navbar">
          <li>
            <Link to="/">Dogs</Link>
          </li>
          <li>
            <Link to="/Editor">Cats</Link>
          </li>
        </ul>
      </div>
    </header>
  );
}
export default Navbar;