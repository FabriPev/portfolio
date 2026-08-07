import { useState, useEffect} from 'react'
import { useForm } from 'react-hook-form'
import { Link } from 'react-router-dom'
import ciudadesService from '../services/ciudades.service'

function Ciudades() {
    useEffect(() => {
        obtenerCiudades()
    }, [])
    const [ciudades, setCiudades] = useState([])
    const { register, handleSubmit} = useForm()

    const obtenerCiudades = async (searchData) => {
        const resultado = await ciudadesService.obtenerCiudades(searchData)
        setCiudades(resultado)
    }
    const eliminarCiudad = async (id) => {
        if (confirm('¿Desea eliminar la ciudad?')) {
            const resultado = await ciudadesService.eliminarCiudad(id)
            await obtenerCiudades()
        }
    }
    const onSubmit = async (searchData) => {
        await obtenerCiudades(searchData)
    }

    return (
            <>
                <h1 className='text-center mt-4 mb-4'>Listado de Ciuades</h1>

                <form className="row gy-2 gx-3 align-items-center mt-5 mb-5" onSubmit={handleSubmit(onSubmit)}>
                    <div className="col-auto">
                        <label className="visually-hidden" htmlFor="autoSizingInput">Name</label>
                        <input type="text" className="form-control" id="autoSizingInput" placeholder="Nombre Ciudad" {...register('ciudad')} />
                    </div>
                    <div className="col-auto">
                        <label className="visually-hidden" htmlFor="autoSizingInputGroup">Username</label>
                        <input type="text" className="form-control" id="autoSizingInputGroup" placeholder="Provincia" {...register('provincia')} />
                    </div>
                    <div className="col-auto">
                    <label className="visually-hidden" htmlFor="autoSizingSelect">Órden</label>
                    <select className="form-select" id="autoSizingSelect" {...register('orden')}>
                        <option value="nombre">Nombre</option>
                        <option value="provincia">Provincia</option>
                        <option value="poblacion">Poblacion</option>
                    </select>
                </div>
                    <div className="col-auto">
                        <button type="submit" className="btn btn-primary"><i className="bi bi-search"></i> Buscar</button>
                    </div>
                    <div className="col-auto">
                        <Link to="/ciudad/0"
                            className="btn btn-primary">
                            <i className="bi bi-plus-circle"></i>
                            &nbsp;Nueva Ciudad
                        </Link>
                    </div>

                </form>

                <div className="col-auto">
                        <button type="submit" className="btn btn-primary"><i className="bi bi-box-arrow-up-right"></i> Mostar Listado</button>
                    </div>
                    <div className="col-auto">
                        <Link to="/ciudad/0"
                            className="btn btn-primary">
                            <i className="bi bi-plus-circle"></i>
                            &nbsp;Nueva Ciudad
                        </Link>
                    </div> 


                <div className="row">
                    <div className="col">
                        <table className="table">
                            <thead>
                                <tr>
                                    <th>Id</th>
                                    <th>Nombre ciudad</th>
                                    <th>Provincia</th>
                                    <th>Poblacion</th>
                                    <th></th>
                                    <th></th>
                                </tr>
                            </thead>
                            <tbody>
                                {ciudades.map((c) => (
                                    <tr key={c.id}>
                                        <td>{c.id}</td>
                                        <td>{c.nombre}</td>
                                        <td>{c.provincia}</td>
                                        <td>{c.poblacion}</td>
                                        <td>
                                            <button className="btn btn-danger" onClick={() => eliminarCiudad(c.id)}>
                                                <i className="bi bi-trash"></i>
                                            </button>
                                        </td>
                                        <td>
                                            <Link to={`/ciudad/${c.id}`} className="btn btn-primary">
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

export default Ciudades