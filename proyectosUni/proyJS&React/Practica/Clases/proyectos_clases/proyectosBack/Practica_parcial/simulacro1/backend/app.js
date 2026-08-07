import express from 'express';
import cors from 'cors';
import sequelize from './db/db.js';
import Peliculas from './models/peliculas.js'; // Importa el modelo de la pelicula
import { Op } from 'sequelize';


const app = express();
const PORT = 3000;
app.use (express.json())
app.use(cors()) // Permite peticiones de otros dominios

sequelize.sync({}); // Sincroniza la base de datos, crea las tablas archivo

app.get('/api/peliculas/', async(req, res) => {
    
    const {titulo, genero, anio} = req.query;
    const donde = {}

    if (titulo){donde.titulo = titulo} // Este es para busqueda exacta
    // if (titulo){donde.titulo = {[Op.like]:`%${titulo}%`}}; Para busqueda parcial
    if (genero){donde.genero= genero}
    if (anio){donde.anio = anio}

    const pelicula = await Peliculas.findAll({where: donde}) // Busca la pelicula por el año en la base de datos, no olvidar el where:
    res.json(pelicula) // Devuelve la pelicula en formato json
})


app.post('/api/peliculas/', async(req,res) => {
    const datosPeliculas = req.body
    const nuevaPelicula = await Peliculas.create(datosPeliculas) // Crea una nueva pelicula en la base de datos
    res.status(201).json(nuevaPelicula) // Devuelve la nueva pelicula creada en formato json
})

app.put('/api/peliculas/:id', async(req,res) => {

    const id =req.params.id
    const añoPelicula = req.body
    await Peliculas.update(añoPelicula, {where:{id:id}}) // Actualiza la pelicula en la base de datos
    res.status(200).json(añoPelicula) // Devuelve la pelicula actualizada en formato json
})

app.delete('/api/peliculas/:id', async(req,res) => {
    const id = req.params.id
    const pelicula = await Peliculas.findByPk(id)
    console.log(pelicula);
    if (pelicula){
        await pelicula.destroy()
        res.sendStatus(200)
    }
    else {res.sendStatus(404)}
})




app.listen(PORT, ()=>{
    console.log(`El servidor está escuchando en el puerto ${PORT}`)
})

