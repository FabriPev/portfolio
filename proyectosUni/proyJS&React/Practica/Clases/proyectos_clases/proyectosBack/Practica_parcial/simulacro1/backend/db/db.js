import {Sequelize} from 'sequelize';
const sequelize = new Sequelize({
    dialect: 'sqlite',
    storage: 'D:/Backup/Documents/Universidad/DDS/Practica/Clases/proyectos_clases/Practica_parcial/simulacro1/datos/peliculas.db'
})
export default sequelize;