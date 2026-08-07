import {Op} from 'sequelize';
import Pelicula from '../models/Pelicula.js';

const getAllPeliculas = async (query) =>{
    try {
        const {orden, titulo, director} = query;

        // Orden (si no se especifica ninguno, será titulo)
        let campoOrden = orden || 'titulo';
        let expOrden = [[campoOrden, 'ASC']];

        // Filtros
        let filtroTitulo = `%${titulo?titulo:''}%`;
        let filtroDirector = `%${director?director:''}%`;

        let expWhere = {
            titulo: {[Op.like]: filtroTitulo},
            director: {[Op.like]: filtroDirector},
        };
        
        // Parámetros
        let parameters = {
            where: expWhere,
            order:expOrden
        }

        const peliculas = await Pelicula.findAll(parameters);
        return peliculas;
    } catch (error) {
        throw error;        
    }

}

const getPelicula = async (id) => {
    try {
        const pelicula = await Pelicula.findByPk(id);
        return pelicula;        
    } catch (error) {
        throw error;                
    }
}

const createPelicula = async (datosPelicula)=>{
    try {
        const pelicula = await Pelicula.create(datosPelicula);
        return pelicula;
    } catch (error) {
        throw error;                
    }
}

const updatePelicula = async (id, datosPelicula)=>{
    try {
        const pelicula = await Pelicula.findByPk(id);
        if (pelicula){
            Object.keys(datosPelicula).forEach(key => {
                if (datosPelicula[key] !== undefined) {
                    pelicula[key] = datosPelicula[key];
                }
            });

            await pelicula.save();
            return pelicula;
        } else {
            throw new Error(`No se encuentra la pelicula`)
        }
    } catch (error) {
        throw error;                
    }    
}

const deletePelicula = async (id)=>{
    try {
        const pelicula = await Pelicula.findByPk(id);
        if (pelicula){
            await pelicula.destroy()
        } else {
            throw new Error(`No se encuentra la pelicula`)
        }
    } catch (error) {
        throw error;                
    }    
}

export default {getAllPeliculas, getPelicula, createPelicula, updatePelicula, deletePelicula}

