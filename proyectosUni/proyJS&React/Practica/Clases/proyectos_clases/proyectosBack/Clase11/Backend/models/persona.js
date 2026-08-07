import { DataTypes } from "sequelize";
import sequelize from "../db.js";

const Persona = sequelize.define('persona', {
    id: {
        type: DataTypes.INTEGER,
        autoIncrement: true,
        primaryKey: true,
    },
    nombre: {
        type: DataTypes.STRING,
        allowNull: false,
    },
    apellido: {
        type: DataTypes.STRING,
        allowNull: false,
    },
    edad : {
        type: DataTypes.INTEGER,
        allowNull: false,
    },
})

export default Persona; // exporta el modelo de la persona