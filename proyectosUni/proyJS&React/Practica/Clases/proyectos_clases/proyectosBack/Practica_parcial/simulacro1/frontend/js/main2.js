addEventListener('DOMContentLoaded', function() {
    const tablaPeliculas = document.querySelector('#tablaPeliculas tbody');
    const btnFiltro = document.getElementById('btnFiltrar');
    const formPelicula = document.getElementById('formPelicula');
    const formActualizar = document.getElementById('formActualizarAnio');
    const formEliminar = document.getElementById('formEliminarPelicula')
    const btnFiltroGenero = document.getElementById('btnFiltrarGenero')
    const btnFiltrarTitulo = document.getElementById('btnFiltrarTitulo')


    MostrarPeliculas(tablaPeliculas);

    btnFiltro.addEventListener('click', function () {
        const anio = document.getElementById('anioFiltro').value;
        const genero = document.getElementById('generoFiltro').value
        const titulo = document.getElementById('tituloFiltro').value
        MostrarPeliculas(tablaPeliculas, anio, titulo, genero)

      });
      
    formPelicula.addEventListener('submit', function () {
        const titulo = document.getElementById('titulo').value;
        const director = document.getElementById('director').value;
        const anio = document.getElementById('anio').value;
        const genero = document.getElementById('genero').value;
        const pelicula = {
            titulo: titulo,
            director: director,
            anio: parseInt(anio),
            genero: genero
        };
        fetch ('http://localhost:3000/api/peliculas', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(pelicula)
        })
        .then (() => formPelicula.reset())
        .then (() => MostrarPeliculas(tablaPeliculas))
    })

    formActualizar.addEventListener('submit', function () {
        const idActualizar = document.getElementById('idPeliculaActualizar').value;
        const anioActualizar = document.getElementById('nuevoAnio').value;
        const peliculaActualizar = {
            anio: parseInt(anioActualizar)
        };
        fetch (`http://localhost:3000/api/peliculas/${idActualizar}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(peliculaActualizar)
        })
        .then (() => formActualizar.reset())
        .then (() => MostrarPeliculas(tablaPeliculas))
    })

    formEliminar.addEventListener('submit', function(){
        const idEliminar = document.getElementById('idPeliculaEliminar').value
        fetch (`http://localhost:3000/api/peliculas/${idEliminar}`,{
            method: 'DELETE'
        })
        .then (()=> formEliminar.reset())
        .then (() => MostrarPeliculas(tablaPeliculas))

    })


    function MostrarPeliculas(tablaPeliculas, anio = '', titulo = '', genero = '') {
        let url = 'http://localhost:3000/api/peliculas';

        const params = new URLSearchParams();
        if (anio)   params.append('anio', anio);
        if (titulo) params.append('titulo', titulo);
        if (genero) params.append('genero', genero);
        if ([anio, titulo, genero].some(val => val)) {
            url += `?${params.toString()}`;
          }

        fetch (url)
        .then(res => res.json())
        .then (peliculas =>{
            tablaPeliculas.innerHTML =''
            let contenido = '';
            peliculas.forEach(p => {
                contenido += `
                    <tr>
                        <td>${p.id}</td>
                        <td>${p.titulo}</td>
                        <td>${p.director}</td>
                        <td>${p.anio}</td>
                        <td>${p.genero}</td>
                    </tr>`;
                
            });
            tablaPeliculas.innerHTML = contenido;
        })
}



})
