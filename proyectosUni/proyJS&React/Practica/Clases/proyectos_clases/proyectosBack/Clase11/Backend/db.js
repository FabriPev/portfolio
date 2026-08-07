import { Sequelize } from "sequelize";


const sequelize = new Sequelize({
    dialect: 'sqlite',
    storage: './datos/personas.db',
});

export default sequelize; // exporta la conexion a la base de datos
