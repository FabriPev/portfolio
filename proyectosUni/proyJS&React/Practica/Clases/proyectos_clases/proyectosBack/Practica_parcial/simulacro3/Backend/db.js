// BASE DE DATOS - DEFECTO
// Esta forma sirve para testing porque no se almacena en la memoria
import { Sequelize } from "sequelize";

const sequelize = new Sequelize({
    dialect: "sqlite",
    storage: "../datos/paciente.db" //CAMBIAR "peliculas" por lo que me piden en la consigna
});

export default sequelize;

/* ALTERNATIVA 
import { Sequelize } from 'sequelize'; 
const sequelize = new Sequelize("sqlite::memory:");

Este bloque crea una instancia de Sequelize utilizando SQLite como motor,
 y define la ubicación del archivo .sqlite que contendrá la base de datos persistente.

*/
