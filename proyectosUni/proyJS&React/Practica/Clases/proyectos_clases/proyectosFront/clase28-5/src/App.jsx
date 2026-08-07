import { useState } from 'react'

import ListinhaTareinhas from './components/ListaTareas'
import NuevaTareinhas from './components/NuevaTarea'


function App() {

  const [tarea, setTarea] = useState('')
  const [tareas, setTareas] = useState([]) 

  function agregarTarea(){
    if (tarea.trim() === "") return
    setTareas([...tareas, tarea])
    setTarea("")

    console.log(tareas)
  }
  function borrarTarea(index){
    console.log("Borrar --> ", index)
    setTareas(tareas.filter((t,i)=>i!==index))
  }

  return (
    <>
    <div className='container'>
      <div className="row">
        <div className="col-6 offset-3">
          <h1 className='text-center mt-5'>Listinha de tareas</h1>
          <NuevaTareinhas tarea={tarea} agregarTarea={agregarTarea} setTarea={setTarea}> </NuevaTareinhas>
          <ListinhaTareinhas tareas={tareas} borrarTarea={borrarTarea}></ListinhaTareinhas>
        </div>
      </div>
    
    
    </div>
    </>

  )
}

export default App
