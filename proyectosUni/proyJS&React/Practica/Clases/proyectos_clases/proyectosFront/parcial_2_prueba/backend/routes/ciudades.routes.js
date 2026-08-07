import { Router } from "express";
import {Op} from 'sequelize';
import ciudadesController from '../controllers/ciudades.controller.js';
import validateToken from "../middleware/validateToken.js";

const ciudadesRouter = new Router();

// ej: GET 
// ciudadesRouter.get('/', validateToken, ciudadesController.getAllciudades)
ciudadesRouter.get('/', ciudadesController.getAllCiudades)

// Ej: GET /25
ciudadesRouter.get('/:id', ciudadesController.getCiudad)

// POST 
ciudadesRouter.post('/', ciudadesController.createCiudad)

// PUT 
ciudadesRouter.put('/:id', ciudadesController.updateCiudad)

// DELETE
ciudadesRouter.delete('/:id', ciudadesController.deleteCiudad)

export default ciudadesRouter;