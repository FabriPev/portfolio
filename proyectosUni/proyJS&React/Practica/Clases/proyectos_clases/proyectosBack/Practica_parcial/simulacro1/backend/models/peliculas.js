import sequelize from "../db/db.js";
import { Model, DataTypes } from "sequelize";

class peliculas extends Model {}
peliculas.init(
  {
    id :{
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
  },
  {
    sequelize,
    modelName: "pelicula",
    tableName: "peliculas",
    timestamps: false,
  }
);

export default peliculas; // exporta el modelo de la pelicula 