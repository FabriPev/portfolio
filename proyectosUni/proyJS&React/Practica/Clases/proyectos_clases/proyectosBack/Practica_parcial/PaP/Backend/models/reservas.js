import sequelize from "../db/db.js"; // Importa la conexion a la base de datos

import {Model, DataTypes} from "sequelize"; // Importa los tipos de datos de sequelize y el modelo

class Reserva extends Model {} // Crea la clase Reserva que extiende de Model

Reserva.init({
    idReserva: {
        type: DataTypes.INTEGER, // Tipo de dato entero
        primaryKey: true, // Clave primaria
        autoIncrement: true // Auto incrementable
    },
    fechaReserva: {
        type: DataTypes.DATE, // Tipo de dato fecha
        allowNull: false // No permite nulos
    },
    nombreJugador: {
        type: DataTypes.STRING, // Tipo de dato cadena
        allowNull: false, // No permite nulos
        validate: {
            len: [1, 30] // Longitud minima y maxima
        }
    },
    numeroCancha: {
        type: DataTypes.INTEGER, // Tipo de dato entero
        allowNull: false, // No permite nulos
    },
    cantidadHoras: {
        type: DataTypes.INTEGER, // Tipo de dato entero
        allowNull: false, // No permite nulos
    },
    Pagada: {
        type :DataTypes.BOOLEAN, // Tipo de dato booleano
        allowNull: false, // No permite nulos
    },
    Importe: {
        type: DataTypes.FLOAT, // Tipo de dato flotante
        }
},
{
    sequelize, // Conexion a la base de datos
    modelName: "Reserva", // Nombre del modelo
    tableName: "Reservas", // Nombre de la tabla
    timestamps: false // No permite timestamps
}
)
