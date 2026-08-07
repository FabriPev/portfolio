import { DataTypes } from "sequelize";
import sequelize from "../db.js";

const Ciudad = sequelize.define('Ciudad', {
    id: { 
        type: DataTypes.INTEGER, 
        autoIncrement: true, 
        primaryKey: true 
    },
    nombre: {
        type: DataTypes.STRING,
        allowNull: false,
    },
    provincia: {
        type: DataTypes.STRING,
        allowNull: true,
    },
    poblacion: {
        type: DataTypes.INTEGER,
    },
}, {
    tableName: 'ciudades',
    timestamps: false
}
);

export default Ciudad;