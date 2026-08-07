# Guía
## Guía para implementar el alta y la modificación en el ejemplo de la clase 25

En la etapa #1 implemetamos el listado y la eliminación. En esta etapa implementaremos el alta y la modificación.

### Etapa 2

### Paso 1: Creación de un nuevo componente e implementación de la navegación

#### 1.1. Creamos un nuevo componente `Pelicula.jsx` con una implementación básica (sólo un encabezado)

```javascript
import { useState } from 'react'

function Pelicula() {

  return (
    <>
      <h1>Datos de la Película</h1>
    </>
  )
}

export default Pelicula
```

#### 1.2. Implementamos la navegación desde el componente `Peliculas.jsx` hacia `Pelicula.jsx` mediante 3 acciones

Definimos la ruta en `App.jsx`. Notese que la ruta tiene un parámetro `id`

```javascript
    import Pelicula from './components/Pelicula'
    ...
    <Routes>
        ...
        <Route path="/pelicula/:id" element={<Pelicula />} />
    </Routes>
```

En `Peliculas.jsx` creamos un botón para el alta en: **Nueva Película** en la parte superior del componente. Este botón pasará el valor `0` para el id. Fijate que en realidad es un `Link` con aspecto de botón 

```javascript
    import { Link } from 'react-router-dom'
    ...
    <div className="col-auto">
        <Link to="/pelicula/0"
            className="btn btn-primary">
            <i className="bi bi-plus-circle"></i>
            &nbsp;Nueva Película
        </Link>
    </div>
```

Creamos un botón para la edición, este botón se mostrará al lado del botón eliminar en cada fila de la tabla

```javascript
    <td>
        <Link to={`/pelicula/${p.id}`} className="btn btn-primary">
            <i className="bi bi-pencil"></i>
        </Link>
    </td>
```

Es muy importante que verifiques el funcionamiento de los dos botones que agregamos: ambos deberían navegar hacia el componente `Pelicula` y en la url tenés que observar el parámetro 0 o el `id` según el caso. Si esto sucede podés seguir adelante

#### 1.2. Recibir el parámetro desde el componente `Pelicula`

Para poder procesar desde el componente `Pelicula` necesitamos recibir el valor del parámetro `id` y tenerlo disponible en una variable. Para ello vamos a usar `useParams` que importamos de `react-router-dom`

```javascript
import { useParams } from 'react-router-dom'
...
const { id } = useParams()
```

Como paso adicional podés usar un `console.log()` y asegurarte de que tenés el valor correcto en la variable `id`

Finalmente vamos a implementar la navegación desde el componente `Pelicula` a `Peliculas` en una función que llamaremos `volver()` y vamos a invocarla desde un botón **Cancelar**. Vamos a usar `useNavigate` desde `react-router-dom`


```javascript
import { useParams, useNavigate } from 'react-router-dom'
...
const navigate = useNavigate()

const volver = () => {
    navigate('/pelicula')
}
...
<button onClick={volver} className="btn btn-warning">Cancelar</button>

```

Con esto queda casi completa la navegación desde y hacia el nuevo componente.

### Paso 2: Cargar los datos de la película cuyo id viene por parámetro

#### 2.1. Implementar el llamado al backend para recuperar los datos de una película

En `services/peliculas.service.js`

```javascript
const obtenerPelicula = async(id) => {
    try {
        const pelicula = await axios.get(`${URL}/${id}`)
        return pelicula.data.data
    } catch (error) {
        
    }
}
...
export default {obtenerPeliculas, obtenerPelicula, eliminarPelicula}
```

#### 2.2. Invocar la función del servicio

En `components/Pelicula.jsx` creamos la función `obtenerPelicula`, agregamos los imports necesarios y, por el momento, mostramos los datos de la película en la consola. Probamos si recupera correctamente la película inspeccionando la consola.

```javascript
import { useState, useEffect } from 'react'
import peliculasService from '../services/peliculas.service'
...

function Pelicula() {
    ...
    useEffect(() => { obtenerPelicula(id) }, [])
    ...
    const obtenerPelicula = async (id) => {
        if (parseInt(id) !== 0) {
            const pelicula = await peliculasService.obtenerPelicula(id)
            console.log(pelicula)
        }
    }
}
```

### Paso 3: Creamos el formulario para que el usuario ingrese los valores de los campos

#### 3.1. Creamos el html del formulario

```javascript
import { useForm } from 'react-hook-form'
...
const { register, handleSubmit, setValue, formState: { errors } } = useForm()
...
return (
    <>
        <div className="row">
            <div className="col">
                <div className="card mt-5">
                    <div className="card-body">
                        <form onSubmit={handleSubmit(onSubmit)}>
                            <fieldset>
                                <legend className="mb-5">Datos Película</legend>
                                <div className="mt-3"><label htmlFor="titulo" className="form-label">Título</label>
                                    <input type="text" name="titulo" className='form-control' 
                                    {...register('titulo')} />
                                </div>
                                <div className="mt-3"><label htmlFor="director" className="form-label">Director</label>
                                    <input type="text" name="director" className='form-control' 
                                    {...register('director')} />
                                </div>
                                <div className="mt-3"><label htmlFor="anio" className="form-label">Año</label>
                                    <input type="text" name="anio" className='form-control' 
                                    {...register('anio')} />
                                </div>
                                <div className="mt-3"><label htmlFor="genero" className="form-label">Género</label>
                                    <input type="text" name="genero" className='form-control' 
                                    {...register('genero')})} />
                                </div>
                            </fieldset>
                            <div className='mt-5'>
                                <input type="submit" value="Guardar" className='btn btn-success ms-2' />
                                <button onClick={volver} className="btn btn-warning ms-2">Cancelar</button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </>
)
}
```

#### 3.2. Creamos la función `onSubmit()` con una implementación provisoria

```javascript
    const onSubmit = async (data) => {
        console.log(data)
    }
```

#### 3.3. Modificamos la implementación de `obtenerPelicula()` para que cargue los valores en el form

```javascript
    const obtenerPelicula = async (id) => {
        if (parseInt(id) !== 0) {
            const pelicula = await peliculasService.obtenerPelicula(id)
            setValue('id', pelicula.id)
            setValue('titulo', pelicula.titulo)
            setValue('director', pelicula.director)
            setValue('anio', pelicula.anio)
            setValue('genero', pelicula.genero)
        }
    }
```

Ya podés probar presionando el botón de modificar en el listado, los valores de la película seleccionada se deberían cargar en los campos del formulario. Si además modificas los valores y presionás el botón **Guardar** en la consola deberías ver los valores que ingresaste

#### 3.4. Agregamos validaciones y mensajes de error

Ahora agregamos validaciones para los distintos campos

```javascript
    return (
        <>
            <div className="row">
                <div className="col">
                    <div className="card mt-5">
                        <div className="card-body">
                            <form onSubmit={handleSubmit(onSubmit)}>
                                <fieldset>
                                    <legend className="mb-5">Datos Película</legend>
                                    <div className="mt-3"><label htmlFor="titulo" className="form-label">Título</label>
                                        <input type="text" name="titulo" className='form-control'
                                            {...register('titulo', { required: 'El título es requerido' })} />
                                        {errors.titulo && <span className='text-danger'>{errors.titulo.message}</span>}
                                    </div>
                                    <div className="mt-3"><label htmlFor="director" className="form-label">Director</label>
                                        <input type="text" name="director" className='form-control'
                                            {...register('director', { required: 'El director es requerido' })} />
                                        {errors.director && <span className='text-danger'>{errors.director.message}</span>}
                                    </div>
                                    <div className="mt-3"><label htmlFor="anio" className="form-label">Año</label>
                                        <input type="text" name="anio" className='form-control'
                                            {...register('anio', { 
                                                required: 'El año es requerido',  
                                                min: {value: 1900, message: 'El año debe ser mayor a 1900'},
                                                max: {value: 2028, message: 'El año debe ser menor a 2028'},
                                            })} />
                                        {errors.anio && <span className='text-danger'>{errors.anio.message}</span>}
                                    </div>
                                    <div className="mt-3"><label htmlFor="genero" className="form-label">Género</label>
                                        <input type="text" name="genero" className='form-control'
                                            {...register('genero', { required: 'El género es requerido' })} />
                                        {errors.genero && <span className='text-danger'>{errors.genero.message}</span>}
                                    </div>
                                </fieldset>
                                <div className='mt-5'>
                                    <input type="submit" value="Guardar" className='btn btn-success ms-2' />
                                    <button onClick={volver} className="btn btn-warning ms-2">Cancelar</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )

```

Y ya podemos probar las validaciones


### Paso 4: Implementamos la modificación y el alta en el servicio

```javascript
const modificarPelicula = async(id, data) => {
    try {
        const pelicula = await axios.put(`${URL}/${id}`, data)
        return pelicula.data
    } catch (error) {
        
    }
}

const agregarPelicula = async(data) => {
    try {
        console.log('Agregar', data)
        const pelicula = await axios.post(`${URL}`, data)
        return pelicula.data.data
    } catch (error) {
        
    }
}
...

export default {obtenerPeliculas, obtenerPelicula, agregarPelicula, modificarPelicula, eliminarPelicula}

```


#### 4.2. Modificamos la implementación de `onSubmit()` para invocar las funciones del servicio

```javascript

const onSubmit = async (data) => {
    if (parseInt(id) === 0) {
        peliculasService.agregarPelicula(data)
    } else {
        peliculasService.modificarPelicula(id, data)
    }

    volver()
}
```