import Express from 'express';
import reservassvc from '../servicies/reservassvc';

const router = Express.Router();


router.get('/reservas', async (req, res) => {
    if (req.query.nombreJugador != undefined && req.query.nombreJugador != "") {
        const data = await reservassvc.getAllByJugador(req.query.nombreJugador);
        res.json(data); // Devuelve todas las reservas en formato json
    }
    else{
        const data = await reservassvc.getAll();
        res.json(data); // Devuelve todas las reservas en formato json
    }






})