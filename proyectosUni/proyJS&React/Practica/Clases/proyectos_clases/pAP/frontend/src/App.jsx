import { useState } from 'react'
import { Inicio } from './components/inicio'
import './App.css'
import { Categorias } from './components/Categorias'
import { BrowserRouter, Route, Routes, Navigate } from "react-router-dom";
import { Menu } from './components/Menu'
import { Footer } from './components/Footer';
import { Articulos } from './components/articulos/Articulos';
import { ModalDialog } from './components/ModalDialog';
import { Usuarios } from "./components/Usuarios";
import {RequireAuth} from "./components/RequiereAuth" ;
import { Login } from "./components/login/Login";



function App() {

  return (
    <>
      <BrowserRouter>
        <ModalDialog />
        <Menu />
        <div className='divBody'>
          <Routes>
              <Route path="/inicio" element={<Inicio />} />
              <Route path="/categorias" element={<Categorias />} />
              <Route path="*" element={<Navigate to="/inicio" replace />} />
              <Route path="/articulos" element={<Articulos/>} />
              <Route
                path="/usuarios"
                element={
                  <RequireAuth>
                    <Usuarios />
                  </RequireAuth>
                }
              />
              <Route path="/login/:componentFrom" element={<Login />} />
              <Route path="*" element={<Navigate to="/inicio" replace />} />

            </Routes>
        </div>
        <Footer />
      </BrowserRouter>
    </>
  )
}

export default App
