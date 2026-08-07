import Reservas from "../models/reservas.js"; // Importa el modelo de reservas
import { Op } from "sequelize"; // Importa el operador Op de sequelize


async function getAll() {
    return await Reservas.findAll({
        order: [['fechaReserva', 'ASC']
                ['numeroCancha', 'ASC']]
    }); // Busca todas las reservas en la base de datos y ordena por fecha y numero de cancha    
}

async function getAllByJugador(nombreJugador) {
    return await Reservas.findAll({
        where : {
            nombreJugador: {
                [Op.startsWith]: nombreJugador // Busca la reserva por el nombre del jugador
            }
        },
        order: [['fechaReserva', 'ASC']
                ['numeroCancha', 'ASC']]
    }); 
}

export default { getAll, getAllByJugador } // Exporta las funciones getReservas y getReserva