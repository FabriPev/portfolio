import { useState, useEffect } from 'react'
import { useForm } from 'react-hook-form'
import { Link } from 'react-router-dom'
import peliculasService from '../services/peliculas.service'

function Peliculas() {
    useEffect(() => { obtenerPeliculas() }, [])
    const [peliculas, setPeliculas] = useState([])
    const { register, handleSubmit } = useForm()

    const obtenerPeliculas = async (searchData) => {
        const data = await peliculasService.obtenerPeliculas(searchData)
        setPeliculas(data)
    }

    const eliminarPelicula = async (id) => {
        if (confirm('¿Desea eliminar la película?')) {
            const resultado = await peliculasService.eliminarPelicula(id)
            await obtenerPeliculas()
        }
    }

    const onSubmit = async (searchData) => {
        await obtenerPeliculas(searchData)
    }

    return (
        <>
            <h1 className='text-center mt-4 mb-4'>Listado de Películas</h1>

            <form className="row gy-2 gx-3 align-items-center mt-5 mb-5" onSubmit={handleSubmit(onSubmit)}>
                <div className="col-auto">
                    <label className="visually-hidden" htmlFor="autoSizingInput">Name</label>
                    <input type="text" className="form-control" id="autoSizingInput" placeholder="Título" {...register('titulo')} />
                </div>
                <div className="col-auto">
                    <label className="visually-hidden" htmlFor="autoSizingInputGroup">Username</label>
                    <input type="text" className="form-control" id="autoSizingInputGroup" placeholder="Director" {...register('director')} />
                </div>
                <div className="col-auto">
                    <label className="visually-hidden" htmlFor="autoSizingSelect">Órden</label>
                    <select className="form-select" id="autoSizingSelect" {...register('orden')}>
                        <option value="titulo">Título</option>
                        <option value="director">Director</option>
                        <option value="anio">Año</option>
                        <option value="genero">Género</option>
                    </select>
                </div>
                <div className="col-auto">
                    <button type="submit" className="btn btn-primary"><i className="bi bi-search"></i> Buscar</button>
                </div>
                <div className="col-auto">
                    <Link to="/pelicula/0"
                        className="btn btn-primary">
                        <i className="bi bi-plus-circle"></i>
                        &nbsp;Nueva Película
                    </Link>
                </div>

            </form>



            <div className="row">
                <div className="col">
                    <table className="table">
                        <thead>
                            <tr>
                                <th>Id</th>
                                <th>Título</th>
                                <th>Director</th>
                                <th>Año</th>
                                <th>Género</th>
                                <th></th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody>
                            {peliculas.map((p) => (
                                <tr key={p.id}>
                                    <td>{p.id}</td>
                                    <td>{p.titulo}</td>
                                    <td>{p.director}</td>
                                    <td>{p.anio}</td>
                                    <td>{p.genero}</td>
                                    <td>
                                        <button className="btn btn-danger" onClick={() => eliminarPelicula(p.id)}>
                                            <i className="bi bi-trash"></i>
                                        </button>
                                    </td>
                                    <td>
                                        <Link to={`/pelicula/${p.id}`} className="btn btn-primary">
                                            <i className="bi bi-pencil"></i>
                                        </Link>
                                    </td>
                                </tr>
                            ))}

                        </tbody>

                    </table>
                </div>
            </div>



        </>
    )
}

export default Peliculas
