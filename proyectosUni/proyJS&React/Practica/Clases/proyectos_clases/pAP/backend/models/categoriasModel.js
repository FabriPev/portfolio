import { DataTypes } from 'sequelize';
import sequelize from './configurarSequelize.js';
const categoria = sequelize.define('Categoria', {
    IdCategoria: { type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true
  },
  Nombre: {
    type: DataTypes.STRING,
    allowNull: false
  }
});

export default categoria;
