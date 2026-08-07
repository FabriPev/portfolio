import {Op} from 'sequelize';
import Ciudad from '../models/Ciudad.js';

const getAllCiudades = async (query) =>{
    try {
        const {orden, nombre, provincia} = query;

        // Orden (si no se especifica ninguno, será nombre)
        let campoOrden = orden || 'nombre';
        let expOrden = [[campoOrden, 'ASC']];

        // Filtros
        let filtroNombre = `%${nombre?nombre:''}%`;
        let filtroProvincia = `%${provincia?provincia:''}%`;

        let expWhere = {
            nombre: {[Op.like]: filtroNombre},
            provincia: {[Op.like]: filtroProvincia},
        };
        
        // Parámetros
        let parameters = {
            where: expWhere,
            order:expOrden
        }

        const ciudades = await Ciudad.findAll(parameters);
        return ciudades;
    } catch (error) {
        throw error;        
    }

}

const getCiudad = async (id) => {
    try {
        const ciudad = await Ciudad.findByPk(id);
        return ciudad;        
    } catch (error) {
        throw error;                
    }
}

const createCiudad = async (datosCiudad)=>{
    try {
        const ciudad = await Ciudad.create(datosCiudad);
        return ciudad;
    } catch (error) {
        throw error;                
    }
}

const updateCiudad = async (id, datosCiudad)=>{
    try {
        const ciudad = await Ciudad.findByPk(id);
        if (ciudad){
            Object.keys(datosCiudad).forEach(key => {
                if (datosCiudad[key] !== undefined) {
                    ciudad[key] = datosCiudad[key];
                }
            });

            await ciudad.save();
            return ciudad;
        } else {
            throw new Error(`No se encuentra la ciudad`)
        }
    } catch (error) {
        throw error;                
    }    
}

const deleteCiudad = async (id)=>{
    try {
        const ciudad = await Ciudad.findByPk(id);
        if (ciudad){
            await ciudad.destroy()
        } else {
            throw new Error(`No se encuentra la ciudad`)
        }
    } catch (error) {
        throw error;                
    }    
}

export default {getAllCiudades, getCiudad, createCiudad, updateCiudad, deleteCiudad}

