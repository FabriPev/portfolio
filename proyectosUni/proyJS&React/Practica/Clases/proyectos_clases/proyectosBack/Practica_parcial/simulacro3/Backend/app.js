//ANTES: en CMD en la carpeta backend
// npm init -y
// npm init sequelize sqlite3 cors express; 
//gitignore de node_modules y package-lock.json en la carpeta backend
//modificar type y dev en el json

// IMPORTACIONES + MENSAJES
//PASO 1: importar - puerto - cors
import express from "express"; //POR DEFECTO
//Express proporciona una serie de funciones que facilitan la creación de rutas de servidor, 
// la gestión de solicitudes y respuestas HTTP,entre otros
import {Op} from "sequelize"; //POR DEFECTO - contiene los operadores para los requerimientos
import cors from "cors"; //POR DEFECTO - funciones en cualquier dominio. PAG 23 DEL APUNTE 11!
import sequelize from "./db.js"; // SIEMPRE CREAR EL ARCHIVO BASE DE DATOS FUERA DE UNA CARPETA PERO DENTRO DE BACK
import Paciente from "./models/paciente.js" //CAMBIAR - models y el archivo con los datos de lo pedido por la consigna


//POR DEFECTO - SIEMPRE ANDAN
const app = express();
const PORT = 3000

//Este middleware analiza las solicitudes entrantes con contenido JSON. 
// Permite que tu aplicación de Express entienda los datos JSON enviados en el cuerpo de la solicitud.
app.use(express.json());

//permite que tu servidor acepte solicitudes desde otros orígenes (dominios). 
app.use(cors());

// Iniciar la base de datos
sequelize.sync({force: true});


// ANDAR PROBANDO EN CMD EN BACKEND CON npm run dev
app.listen(PORT, () =>{
    console.log(`El servidor se está escuchando en el puerto: ${PORT}`) // EL MISMO PUERTO EN LAS RUTAS DE LOS MENSAJES HTTPS
});

/*RECUPERAR DATOS - "Usuario" es "Paciente"
 1. RECUPERAR TODOS LOS RESGITROS
const usuarios = await Usuario.findAll(); 

2.Obtener un único registro
const usuario = await Usuario.findOne({ where: { id: 5 } }); 

3.FILTROS
const usuarios = await Usuario.findAll({
 where: { 
 apellido: { [Op.like]: '%ez'} // para traer todos los apellidos terminados en 'ez'   
    } 
        });
*/

/*
const usuariosOrdenados = await Usuario.findAll({ 
where: {     
[Op.and]: [       
{ apellido: { [Op.like]: '%ez' } },      
  { [Op.not]: { id: [1, 2, 3] } }    
    ]  
   }, 
   order: [['apellido', 'ASC']] // ordenar los resultados del findAll
   }); 
*/

//4. ORDEN
 // Orden (si no se especifica ninguno, será apellido)
 //let campoOrden = req.query.orden || 'apellido';
 //let expOrden = [[campoOrden, 'ASC']];

//REQUERIMIENTOS DE LA CONSIGNA - "nombre".http - rutas datas en la consignas

//Agregar pacientes - POST //ruta dada en la consigna
app.post('/api/pacientes', async (req, res) => {
    try {
        if (!req.body.Nombre || !req.body.Propietario) {
            return res.status(400).json({ message: "Faltan datos requeridos (Nombre o Propietario)" });
        }
        const datosPaciente = req.body;
        const nuevoPaciente = await Paciente.create(datosPaciente);
        res.status(201).json(nuevoPaciente);
    } catch (error) {
        console.error("Error en la creación del paciente:", error);
        res.status(500).json({ message: "Error interno del servidor", error: error.message });
    }
});

/*
//1. Obtener todas los pacientes
app.get('/api/pacientes', async (req, res) => {
    try {
        const pacientes = await Paciente.findAll();
        res.json(pacientes);
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: "Error al obtener los pacientes", error: error.message });
    }
});



//2.Pacientes filtrados por el nombre del propietario -GET
app.get('/api/pacientes', async (req, res) => {
    try {
        const filtroNombre = `%${req.query.nombre ? req.query.nombre : ''}%`;;

        const expWhere = {
            Propietario: { [Op.like]: filtroNombre },
        };

        const pacientes = await Paciente.findAll({
            where: expWhere
        });

        res.json(pacientes);
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: "Error al obtener los pacientes filtrados", error: error.message });
    }
});
*/

//PARA QUE ANDE EL 1 Y EL 2
app.get('/api/pacientes', async (req, res) => {
    try {
        const expWhere = req.query.Propietario 
            ? { Propietario: { [Op.like]: `%${req.query.Propietario}%` } } //Verifica si en la URL de la petición hay un parámetro llamado Propietario.
            : {};//Deja el objeto vacío ({}). Esto significa que la consulta no aplicará ningún filtro.

        const pacientes = await Paciente.findAll({ where: expWhere });
        res.json(pacientes);
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: "Error al obtener los pacientes", error: error.message });
    }
});
//where es una opción de consulta en Sequelize que te permite filtrar los resultados que obtienes de la base de datos
//Esta variable contiene el objeto de condiciones (where) que usarás para filtrar los resultados.



//3.Obtener un paciente específico por su ID.
app.get('/api/pacientes/:id', async (req, res)=>{
    const id = req.params.id;
    const paciente = await Paciente.findByPk(id);
    res.json(paciente);
})

//4. Actualizar un paciente por su ID.
app.put('/api/pacientes/:id', async (req, res) => {
    // Recibimos los datos actualizados en el cuerpo de la petición (JSON)
    const datosPaciente = req.body;
    const id = req.params.id;

    try {
        // Buscamos al paciente por su ID
        const paciente = await Paciente.findByPk(id);

        if (paciente) {
            // Si se encuentra el paciente, actualizamos los datos
            paciente.Nombre = datosPaciente.Nombre || paciente.Nombre; // Si no se recibe 'Nombre', no lo modificamos
            paciente.Propietario = datosPaciente.Propietario || paciente.Propietario; 
            paciente.Telefono = datosPaciente.Telefono || paciente.Telefono; // 

            // Guardamos los cambios en la base de datos
            await paciente.save();

            // Respondemos con un estado 200 (OK) para indicar que la actualización fue exitosa
            res.status(200).json({ message: 'Paciente actualizado correctamente' });
        } else {
            // Si no se encuentra el paciente, respondemos con un estado 404 (No encontrado)
            res.status(404).json({ message: 'Paciente no encontrado' });
        }
    } catch (error) {
        // Si ocurre un error, respondemos con un estado 500 (Error interno del servidor)
        res.status(500).json({ message: 'Error al actualizar el paciente', error: error.message });
    }
});

//5.Eliminar un paciente específico por su ID.
app.delete('/api/pacientes/:id', async (req, res) => {
    const id = req.params.id;
    const paciente = await Paciente.findByPk(id);
    if (paciente){
        await paciente.destroy();
        res.sendStatus(200);
    } else {
        res.sendStatus(404);
    }
})