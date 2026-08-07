import { useState } from 'react'

function ListinhaTareinhas({tareas, borrarTarea}) {

    return (
    <>
    <ul className="list-group mt-5">
        {tareas.map((tarea, index)=><li key = {index} className="list-group-item d-flex justify-content-between align-items-center">
            {tarea}
            <button className='btn btn-danger' onClick={()=> borrarTarea(index)}>x</button>
        </li>)}


       {/* <li className="list-group-item d-flex justify-content-between align-items-center">
            A list item
            <button className='btn btn-danger'>x</button>
        </li>
        <li className="list-group-item d-flex justify-content-between align-items-center">
            A second list item
            <button className='btn btn-danger'>x</button>  </li>
        <li className="list-group-item d-flex justify-content-between align-items-center">
            A third list item
            <button className='btn btn-danger'>x</button>  </li*/}
    </ul>
    </>
    )
}
export default ListinhaTareinhas
