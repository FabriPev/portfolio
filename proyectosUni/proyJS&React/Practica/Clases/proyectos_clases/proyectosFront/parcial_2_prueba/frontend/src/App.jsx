import { useState } from 'react'
import './App.css'
import {BrowserRouter, Routes, Route, Link, NavLink} from 'react-router-dom'
import Inicio from './components/Inicio'
import Acerca from './components/Acerca'
import Ciudades from './components/Ciudades'
import Ciudad from './components/Ciudad'

function App() {
  const [count, setCount] = useState(0)

  return (
    <BrowserRouter>
      <nav className="navbar navbar-expand-lg bg-body-tertiary" data-bs-theme="dark">
        <div className="container-fluid">
          <a className="navbar-brand" href="#">ArgData</a>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarText">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item">
                <NavLink to='/inicio' className={({ isActive }) => isActive ? "nav-link active" : "nav-link"}>Inicio</NavLink>
              </li>
              <li className="nav-item">
                <NavLink to='/acerca' className={({ isActive }) => isActive ? "nav-link active" : "nav-link"}>Acerca</NavLink>
              </li>
              <li className="nav-item">
                <NavLink to='/ciudades' className={({ isActive }) => isActive ? "nav-link active" : "nav-link"}>Ciudades</NavLink>
              </li>
            </ul>
          </div>
        </div>
      </nav>
      <div className="container">
        <div className="row">
          <div className="col-lg-6 offset-lg-3">
            <Routes>
              <Route path="/" element={<Inicio />} />
              <Route path="/inicio" element={<Inicio />} />
              <Route path="/acerca" element={<Acerca />} />
              <Route path="/ciudades" element={<Ciudades/>} />
              <Route path="/ciudades/:id" element={<Ciudad />} />
            </Routes>
          </div>
        </div>
      </div>

    </BrowserRouter>
  )
}

export default App
