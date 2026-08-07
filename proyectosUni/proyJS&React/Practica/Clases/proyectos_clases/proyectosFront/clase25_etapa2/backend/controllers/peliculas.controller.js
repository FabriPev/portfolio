import {Op} from 'sequelize';
import Pelicula from '../models/Pelicula.js';
import peliculasService from '../services/peliculas.service.js';
import validateToken from '../middleware/validateToken.js';

const getAllPeliculas = async (req, res) => {
    try {
        const peliculas = await peliculasService.getAllPeliculas(req.query);
        res.send({status: "OK", data: peliculas});
    } catch (error) {
        res.status(500).send ({status:"FAILED", data: {error: error?.message || error}})
        return;
    }
}

const getPelicula = async (req, res)=>{
    const id = req.params.id;
    if (!id || isNaN(id)){
        res.status(500).send ({status:"FAILED", data: {error: "Debe especificar un id numérico"}})
        return;

    }
    try {
        const pelicula = await peliculasService.getPelicula(id);
        if (pelicula){
            res.send({status: "OK", data: pelicula});
        }
        else {
            res.status(404).send ({status:"FAILED", data: {error: "No se encontró la pelicula"}})
        return;
        }

    }
    catch (error) {
        res.status(500).send ({status:"FAILED", data: {error: error?.message || error}})
        return;
    }
}

const createPelicula = async(req, res)=>{
    const {body: datosPelicula} = req;
    if (
        !datosPelicula.titulo ||
        !datosPelicula.director ||
        !datosPelicula.genero ||
        !datosPelicula.anio
    ){
        res.status(500).send ({status:"FAILED", data: {error: "Debe proveer: título, director, género y año"}})
        return;
    }
    else {
        try {
            const pelicula = await peliculasService.createPelicula(datosPelicula);
            res.status(201).send({status: "OK", data: pelicula});    
        } catch (error) {
            res.status(500).send ({status:"FAILED", data: {error: error?.message || error}})
            return;
        }
    }
}

const updatePelicula = async(req, res)=>{
    const id = req.params.id;
    const {body: datosPelicula} = req;
    if (!id || isNaN(id)){
        res.status(400).send ({status:"FAILED", data: {error: "Debe especificar un id numérico"}})
        return;
    }
    try {
        await peliculasService.updatePelicula(id, datosPelicula);
        res.status(200).send({status: "OK", data: 'Pelicula actualizada'});    
    }
    catch (error){
        res.status(500).send ({status:"FAILED", data: {error: error?.message || error}})
        return;
    }    
}

const deletePelicula = async(req, res)=>{
    const id = req.params.id;
    if (!id || isNaN(id)){
        res.status(400).send ({status:"FAILED", data: {error: "Debe especificar un id numérico"}});
        return;
    }
    try {
        await peliculasService.deletePelicula(id);
        res.status(200).send({status: "OK", data: 'Pelicula borrada'});    
    }
    catch (error) {
        res.status(500).send ({status:"FAILED", data: {error: error?.message || error}});
        return;
    }    
}

export default {getAllPeliculas, getPelicula, createPelicula, updatePelicula, deletePelicula}