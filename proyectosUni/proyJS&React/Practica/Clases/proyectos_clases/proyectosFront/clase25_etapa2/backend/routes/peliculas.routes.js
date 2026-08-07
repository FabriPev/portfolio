import { Router } from "express";
import {Op} from 'sequelize';
import peliculasController from '../controllers/peliculas.controller.js';
import validateToken from "../middleware/validateToken.js";

const peliculasRouter = new Router();

// ej: GET 
// peliculasRouter.get('/', validateToken, peliculasController.getAllPeliculas)
peliculasRouter.get('/', peliculasController.getAllPeliculas)

// Ej: GET /25
peliculasRouter.get('/:id', peliculasController.getPelicula)

// POST 
peliculasRouter.post('/', peliculasController.createPelicula)

// PUT 
peliculasRouter.put('/:id', peliculasController.updatePelicula)

// DELETE
peliculasRouter.delete('/:id', peliculasController.deletePelicula)

export default peliculasRouter;