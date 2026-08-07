import { useState, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { useForm } from 'react-hook-form'
import peliculasService from '../services/peliculas.service'

function Pelicula() {
    const { id } = useParams()
    const navigate = useNavigate()
    const { register, handleSubmit, setValue, formState: { errors } } = useForm()
    useEffect(() => { obtenerPelicula(id) }, [])

    const volver = () => {
        navigate('/peliculas')
    }

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

    const onSubmit = async (data) => {
        if (parseInt(id) === 0) {
            peliculasService.agregarPelicula(data)
        } else {
            peliculasService.modificarPelicula(id, data)
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
}

export default Pelicula
