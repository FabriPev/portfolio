import express from 'express';
import categoriasmock from './routes/categoriasmock.js';
import categoriasRouter from './routes/categorias.js';
import articulosRouter from './routes/articulos.js';
import cors from 'cors';
import inicializarBase from './models/inicializarBase.js';
import SeguridadRouter from './routes/seguridad.js';
import usuariosRouter from './routes/usuarios.js';
import { fileURLToPath } from 'url';


//Crear serividor express
const app = express();
app.use(express.json()); //Para poder recibir datos en formato JSON

//Controlador de la ruta raíz
app.get('/', (req, res) => {
    res.send('Backend inicial dds-backend!');
})

//levantamiento del servidor
const port = 3000;
app.locals.fechaInicio = new Date(); //Fecha de inicio d    el servidor



if (process.argv[1] === fileURLToPath(import.meta.url)) {
  inicializarBase().then(() => {
    app.listen(port, () => {
      console.log(`sitio escuchando en el puerto ${port}`);
    });
  });
}



//Rutas
app.use(categoriasmock);
app.use(categoriasRouter);
app.use(articulosRouter);
app.use(
  cors({
    origin: "*", // origin: 'https://dds-frontend.azurewebsites.net'
  })
);
app.use(SeguridadRouter);
app.use(usuariosRouter);
app.get('/_isalive', (req, res) => {
  try {
    const currentDirectory = process.cwd();
    res.status(200).send(`Ejecutandose desde: ${currentDirectory}`);
  } catch (error) {
    console.error('Error en /_isalive:', error);
    res.status(500).send('Error interno del servidor');
  }
});

app.use((req, res, next) => {
  res.status(404).send("No encontrada!");
});

export default app;