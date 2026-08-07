import express from 'express'
import cors from 'cors' // Importa el paquete cors para permitir peticiones de otros dominios, en este caso de la aplicacion frontend
import sequelize from './db.js'; // Importa la conexion a la base de datos
import Persona from './models/persona.js'; // Importa el modelo de la persona



const app = express(); //Crea el servidor, va siempre
const PORT = 3001
app.use (express.json())
app.use(cors()) // Permite peticiones de otros dominios

//Conexion a la base de datos

sequelize.sync(); // Sincroniza la base de datos, crea las tablas si no existen  y archivo
// sequelize.sync({force: true}) Sincroniza la base de datos, crea las tablas si no existen y archivo, borra las tablas si existen y las vuelve a crear



// RUTAS

// GET /api/personas
app.get('/api/personas',  async(req, res) =>{
    //const sexo = req.query.sexo
    //const apellido = req.query.apellido
    //res.send(`Obtener todas las personas con sexo ${sexo} y apellido ${apellido}`)

    const personas = await Persona.findAll() // Busca todas las personas en la base de datos
    res.json(personas) // Devuelve todas las personas en formato json


} )
// GET /api/personas/25

app.get('/api/personas/:id', async(req, res) => {
    const id = req.params.id
    //res.send(`Obtener la personas con el id o7 ${id}`)
    const perssona = await Persona.findByPk(id) // Busca la persona por el id en la base de datos
    res.json(perssona) // Devuelve la persona en formato json

})

// POST /api/personas
app.post('/api/personas/', async(req,res) => {
    const datosPersonas = req.body
    const nuevaPersona = await Persona.create(datosPersonas) // Crea una nueva persona en la base de datos
    res.status(201).json(nuevaPersona) // Devuelve la nueva persona creada en formato json

})

// PUT /api/personas/  ACTUALIZAR
app.put('/api/personas/:id', async(req,res) => {
    const datosPersonas = req.body
    const id = req.params.id

     const persona = await Persona.findByPk(id) // Busca la persona por el id en la base de datos
     if (persona){
        persona.edad = datosPersonas.edad // Actualiza la edad de la persona
        await persona.save() // Guarda los cambios en la base de datos
        res.sendStatus(200) // Devuelve un estado 200 (OK)
     }
     else {res.sendStatus(404) // Devuelve un estado 404 (No encontrado)
        }

    
    //console.log(req.body)
    //res.send('Modica una persona')
})

app.delete('/api/personas/:id', async(req, res) => {
    const id = req.params.id
    const persona = await Persona.findByPk(id) // Busca la persona por el id en la base de datos
    if (persona){
        await persona.destroy() // Elimina la persona de la base de datos
        res.sendStatus(200) // Devuelve un estado 200 (OK)
    }
    else {res.sendStatus(404) // Devuelve un estado 404 (No encontrado)
    }


    // res.send ('Elimina una persona')
})




app.listen(PORT, () => {console.log(`El servidor esta escuchando el puerto ${PORT}`)}
)// Pone la aplicacion para escuchar las peticiones

// en json usar type : module y el dev --watch

// npm istall sqlite3 sequelize
// npm install cors