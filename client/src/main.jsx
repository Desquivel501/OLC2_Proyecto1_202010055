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
import {Reporte_TS}  from './views/Reporte_TS'

import './index.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <NavbarComponent />
      <Routes>
        <Route path='/' element={<App />} />
        <Route path='/about' element={<About />} />
        <Route path='/reporte_ts' element={<Reporte_TS />} />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
)
