import React from 'react'
import ReactDOM from 'react-dom/client'
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";


import { NavbarComponent } from './components/NavbarComponent';

import App from './App'
import {About}  from './views/About'
import {Reportes}  from './views/Reportes'

import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <NavbarComponent />
      <Routes>
        <Route path='/' element={<App />} />
        <Route path='/about' element={<About />} />
        <Route path='/reportes' element={<Reportes />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
)
