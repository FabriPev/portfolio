import {Op} from 'sequelize';
import Ciudad from '../models/Ciudad.js';
import ciudadesService from '../services/ciudades.service.js';
import validateToken from '../middleware/validateToken.js';

const getAllCiudades = async (req, res) => {
    try {
        const ciudades = await ciudadesService.getAllCiudades(req.query);
        res.send({status: "OK", data: ciudades});
    } catch (error) {
        res.status(500).send ({status:"FAILED", data: {error: error?.message || error}})
        return;
    }
}

const getCiudad = async (req, res)=>{
    const id = req.params.id;
    if (!id || isNaN(id)){
        res.status(500).send ({status:"FAILED", data: {error: "Debe especificar un id numérico"}})
        return;

    }
    try {
        const ciudad = await ciudadesService.getCiudad(id);
        if (ciudad){
            res.send({status: "OK", data: ciudad});
        }
        else {
            res.status(404).send ({status:"FAILED", data: {error: "No se encontró la ciudad"}})
        return;
        }

    }
    catch (error) {
        res.status(500).send ({status:"FAILED", data: {error: error?.message || error}})
        return;
    }
}

const createCiudad = async(req, res)=>{
    const {body: datosCiudad} = req;
    if (
        !datosCiudad.nombre ||
        !datosCiudad.provincia ||
        !datosCiudad.poblacion
    ){
        res.status(500).send ({status:"FAILED", data: {error: "Debe proveer: nombre, provincia, población"}})
        return;
    }
    else {
        try {
            const ciudad = await ciudadesService.createCiudad(datosCiudad);
            res.status(201).send({status: "OK", data: ciudad});    
        } catch (error) {
            res.status(500).send ({status:"FAILED", data: {error: error?.message || error}})
            return;
        }
    }
}

const updateCiudad = async(req, res)=>{
    const id = req.params.id;
    const {body: datosCiudad} = req;
    if (!id || isNaN(id)){
        res.status(400).send ({status:"FAILED", data: {error: "Debe especificar un id numérico"}})
        return;
    }
    try {
        await ciudadesService.updateCiudad(id, datosCiudad);
        res.status(200).send({status: "OK", data: 'Ciudad actualizada'});    
    }
    catch (error){
        res.status(500).send ({status:"FAILED", data: {error: error?.message || error}})
        return;
    }    
}

const deleteCiudad = async(req, res)=>{
    const id = req.params.id;
    if (!id || isNaN(id)){
        res.status(400).send ({status:"FAILED", data: {error: "Debe especificar un id numérico"}});
        return;
    }
    try {
        await ciudadesService.deleteCiudad(id);
        res.status(200).send({status: "OK", data: 'Ciudad borrada'});    
    }
    catch (error) {
        res.status(500).send ({status:"FAILED", data: {error: error?.message || error}});
        return;
    }    
}

export default {getAllCiudades, getCiudad, createCiudad, updateCiudad, deleteCiudad}