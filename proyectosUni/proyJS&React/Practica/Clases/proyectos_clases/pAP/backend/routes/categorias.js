import express from 'express';
import categoria from '../models/categoriasModel.js'


const router = express.Router();

router.get('/api/categorias', async function (req, res) {
  try {
    const categorias = await categoria.findAll();
    res.json(categorias);
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Error al obtener las categorías' });
  }
});

router.get('/api/categorias/:id', async function (req, res) {
  try {
    const categoriaEncontrada = await categoria.findByPk(req.params.id);
    if (categoriaEncontrada) {
      res.json(categoriaEncontrada);
    } else {
      res.status(404).json({ message: 'Categoría no encontrada' });
    }
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Error al obtener la categoría' });
  }
});

export default router;