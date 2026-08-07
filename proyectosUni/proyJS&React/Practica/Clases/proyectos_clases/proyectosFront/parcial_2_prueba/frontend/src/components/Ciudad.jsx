import { useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { useForm } from 'react-hook-form'
import ciudadesService from '../services/ciudades.service'

function Ciudad() {
    const { id } = useParams()
    const navigate = useNavigate()
    const { register, handleSubmit, setValue, formState: { errors } } = useForm()
    useEffect(() => { obtenerCiudad(id) }, [])

    const volver = () => {
        navigate('/ciudades')
    }

    const obtenerCiudad = async (id) => {
        if (parseInt(id) !== 0) {
            const ciudad = await ciudadesService.obtenerCiudades(id)
            setValue('id', ciudad.id)
            setValue('nombre', ciudad.nombre)
            setValue('provincia', ciudad.provincia)
            setValue('poblacion', ciudad.poblacion)
        }
    }
    const onSubmit = async (data) => {
        if (parseInt(id) === 0) {
            ciudadesService.agregarCiudades(data)
        } else {
            ciudadesService.modificarCiudades(id, data)
        }

        volver()
    }


    return (
        <>
            <div className="row">
                <div className="col">
                    <div className="card mt-5">
                        <div className="card-body">
                            <form onSubmit={handleSubmit(onSubmit)}>
                                <fieldset>
                                    <legend className="mb-5">Datos de la Ciudad</legend>
                                    <div className="mt-3"><label htmlFor="nombre" className="form-label">Nombre</label>
                                        <input type="text" name="nombre" className='form-control'
                                            {...register('nombre', { required: 'El Nombre es requerido' })} />
                                        {errors.nombre && <span className='text-danger'>{errors.nombre.message}</span>}
                                    </div>
                                    <div className="mt-3"><label htmlFor="provincia" className="form-label">Provincia</label>
                                        <input type="text" name="provincia" className='form-control'
                                            {...register('provincia', { required: 'La provincia es requerido' })} />
                                        {errors.provincia && <span className='text-danger'>{errors.provincia.message}</span>}
                                    </div>
                                    <div className="mt-3"><label htmlFor="poblacion" className="form-label">Poblacion</label>
                                        <input type="text" name="poblacion" className='form-control'
                                            {...register('poblacion', { 
                                                required: 'La poblacion es requerido',  
                                                min: {value: 1000, message: 'La poblacion debe ser mayor a 1900'},
                                            })} />
                                        {errors.poblacion && <span className='text-danger'>{errors.poblacion.message}</span>}
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
export default Ciudad