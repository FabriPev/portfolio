import { useState } from 'react'

function Acerca() {

  return (
    <div className="container mt-5">
      <h2 className="text-center mb-4">Acerca de 🧐</h2>
      <p>
        ArgData nació con el objetivo de facilitar el acceso y la gestión de datos urbanos 🏘️.
      </p>
      <p>Permite a investigadores, gobiernos y ciudadanos:</p>
      <ul className="list-group mb-3">
        <li className="list-group-item">🔍 Consultar datos actualizados de ciudades.</li>
        <li className="list-group-item">📈 Visualizar estadísticas demográficas y económicas.</li>
        <li className="list-group-item">🗺️ Comparar diferentes regiones geográficas.</li>
      </ul>
      <p>Creado con ❤️ por alumnos de DDS.</p>
    </div>
  );
}

export default Acerca
