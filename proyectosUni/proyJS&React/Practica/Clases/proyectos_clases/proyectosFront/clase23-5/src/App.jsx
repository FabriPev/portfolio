import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Componente1 from './Componente1'

function App() {
  return (
    <div className="App">
      <h1>Mi primer sitio con react</h1>

      <Componente1 nombre="letix" apellido="Peveraro"/>
      <Componente1 nombre="lolman" apellido="Contreras"/>
      <Componente1 nombre="brick" apellido="Aguero"/>
      <Componente1 nombre="mastusalen24" apellido="Bricca"/>
      <Componente1 nombre="formaDelOso"/>


    </div>
  )

  
}

export default App
