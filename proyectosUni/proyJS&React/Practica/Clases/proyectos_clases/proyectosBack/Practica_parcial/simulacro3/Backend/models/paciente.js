//DATOS
import { Model,DataTypes } from "sequelize"; //POR DEFECTO -  Para tener disponibles los tipos de datos incluidos en Sequelize
import sequelize from "../db.js"; // /POR DEFECTO CUANDO EL ARCHIVO ESTÁ SÓLO EN LA CARPETA BACKEND

// DATOS DE LA CONSIGNA
const Paciente = sequelize.define("Paciente", {
    IdPaciente: { type: DataTypes.INTEGER, primaryKey: true, allowNull: false, autoIncrement: true },
    Nombre: { type: DataTypes.STRING, allowNull: false },
    Propietario: { type: DataTypes.STRING, allowNull: false },
    Telefono: { type: DataTypes.STRING, allowNull: true },  
});



class paciente extends Model{}
paciente.init({
    IdPaciente:{
        type: DataTypes.INTEGER,
        primaryKey: true,
        allowNull: false,
        autoIncrement: true
    },
    Nombre: {
        type: DataTypes.STRING,
        allowNull: false
    },
    Propietario: {
        type: DataTypes.STRING,
        allowNull: false
    },
    Telefono:{
        type:  DataTypes.STRING,
        allowNull: true
    }

},
{
    sequelize,
    modelName: 'Paciente',
    tableName: 'pacientes',
    timestamps: false


});



export default paciente; // SEIMPRE SE HACE PARA ACCEDER A LOS DATOS DESPUÉS