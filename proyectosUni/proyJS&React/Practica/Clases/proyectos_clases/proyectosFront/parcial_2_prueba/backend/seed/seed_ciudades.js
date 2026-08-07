// No importes este módulo desde tu app
// Tiene el único propósito de inicializar los datos 

import { Sequelize, DataTypes } from 'sequelize';
import fs from 'fs';

const sequelize = new Sequelize({
    dialect: 'sqlite',
    storage: process.env.DB_PATH || "./datos/datos.db",
});

// Model Ciudad
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
});

// Cargar ciudades desde JSON
const inicializarDesdeJSON = async (filePath) => {
    try {
        const data = fs.readFileSync(filePath, 'utf8');
        const ciudades = JSON.parse(data);

        if (!Array.isArray(ciudades) || ciudades.length === 0) {
            throw new Error('Archivo JSON vacío o no válido.');
        }

        await sequelize.sync({ force: true });
        await Ciudad.bulkCreate(ciudades);
        console.log('Ciudades cargadas.');
    } catch (error) {
        console.error('Error cargando ciudades:', error.message);
    } finally {
        await sequelize.close();
    }
};

export default {inicializarDesdeJSON}