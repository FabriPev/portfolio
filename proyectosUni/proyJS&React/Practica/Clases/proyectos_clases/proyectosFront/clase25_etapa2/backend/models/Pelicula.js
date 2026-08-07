import { DataTypes } from "sequelize";
import sequelize from "../db.js";

const Pelicula = sequelize.define('Pelicula', {
    id: { 
        type: DataTypes.INTEGER, 
        autoIncrement: true, 
        primaryKey: true 
    },
    titulo: {
        type: DataTypes.STRING,
        allowNull: false,
    },
    director: {
        type: DataTypes.STRING,
        allowNull: true,
    },
    anio: {
        type: DataTypes.INTEGER,
    },
    genero: {
        type: DataTypes.STRING,
        allowNull: true,
    },
}, {
    tableName: 'peliculas',
    timestamps: false
}
);

export default Pelicula;