import Express from 'express';
import ReservasModel from '../models/reserva.js'; // Importa el modelo de reserva
import cors from 'cors'; // Importa cors para permitir peticiones de otros dominios
import db from './db/db.js'; // Importa la conexion a la base de datos
import Reservas from './routes/reservas.js'; // Importa las rutas de reservas

const app = Express(); // Crea el servidor
app.use(Express.json()); // Permite el uso de json en las peticiones
app.use(cors()); // Permite peticiones de otros dominios
app.use (Reservas); // Usa las rutas de reservas
