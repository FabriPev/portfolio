import axios from 'axios'

const URL = 'http://localhost:3200/api/ciudades'

const obtenerCiudades = async(searchData) => {
    try {
        const queryString = new URLSearchParams(searchData).toString()
        const ciuades = await axios.get(`${URL}?${queryString}`)
        return ciuades.data.data
        
    } catch (error) {
        
    }
}

const obtenerCiudad = async(id) => {
    try {
        const ciudades = await axios.get(`${URL}/${id}`)
        return ciudades.data.data
    } catch (error) {
        
    }
}

const modificarCiudades = async(id, data) => {
    try {
        const ciudades = await axios.put(`${URL}/${id}`, data)
        return ciudades.data
    } catch (error) {
        
    }
}

const agregarCiudades = async(data) => {
    try {
        console.log('Agregar', data)
        const ciudades = await axios.post(`${URL}`, data)
        return ciudades.data.data
    } catch (error) {
        
    }
}

const eliminarCiudad = async(id)=> {
    try {
        const resultado = await axios.delete(`${URL}/${id}`)
        return resultado
    } catch (error) {
        
    }
}

export default {obtenerCiudades, obtenerCiudad, agregarCiudades, modificarCiudades, eliminarCiudad}