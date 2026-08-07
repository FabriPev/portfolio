import axios from 'axios'

const URL = 'http://localhost:3200/api/peliculas'

const obtenerPeliculas = async(searchData) => {
    try {
        const queryString = new URLSearchParams(searchData).toString()
        const peliculas = await axios.get(`${URL}?${queryString}`)
        return peliculas.data.data
        
    } catch (error) {
        
    }
}

const obtenerPelicula = async(id) => {
    try {
        const pelicula = await axios.get(`${URL}/${id}`)
        return pelicula.data.data
    } catch (error) {
        
    }
}

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

const eliminarPelicula = async(id)=> {
    try {
        const resultado = await axios.delete(`${URL}/${id}`)
        return resultado
    } catch (error) {
        
    }
}

export default {obtenerPeliculas, obtenerPelicula, agregarPelicula, modificarPelicula, eliminarPelicula}