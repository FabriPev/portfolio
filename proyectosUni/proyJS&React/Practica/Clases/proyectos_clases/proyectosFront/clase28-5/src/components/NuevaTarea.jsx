import { useState } from 'react'

function NuevaTareinhas({tarea, agregarTarea, setTarea}) {
return (
<>
<div className='input-group mt-5'>
    <input type='text' className='form-control' value= {tarea} onChange={(e) =>{setTarea(e.target.value)}}></input>
    <button className='btn btn-dark' onClick={agregarTarea}>Agregar</button>



</div></>
)
}
export default NuevaTareinhas
