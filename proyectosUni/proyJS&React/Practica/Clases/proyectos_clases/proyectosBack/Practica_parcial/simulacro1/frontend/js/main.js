// JavaScript principal del frontend
document.addEventListener('DOMContentLoaded', function() {
    // Elementos del DOM
    const formPelicula = document.getElementById('formPelicula');
    const tablaPeliculas = document.getElementById('tablaPeliculas');
    const filtroAnio = document.getElementById('filtroAnio');
    const btnFiltrar = document.getElementById('btnFiltrar');
    const btnLimpiar = document.getElementById('btnLimpiar');
    
    // URL base de la API
    const API_URL = 'http://localhost:3000/api/peliculas';
    
    // Cargar películas al iniciar
    cargarPeliculas();
    
    // Evento para enviar el formulario
    formPelicula.addEventListener('submit', function(e) {
        e.preventDefault();
        agregarPelicula();
    });
    
    // Evento para filtrar películas
    btnFiltrar.addEventListener('click', function() {
        const anio = filtroAnio.value;
        if (anio) {
            cargarPeliculas(anio);
        } else {
            cargarPeliculas();
        }
    });
    
    // Evento para limpiar filtro
    btnLimpiar.addEventListener('click', function() {
        filtroAnio.value = '';
        cargarPeliculas();
    });
    
    // Función para cargar películas
    function cargarPeliculas(anio = null) {
        let url = API_URL;
        if (anio) {
            url = `${API_URL}/${anio}`;
        }
        
        fetch(url)
            .then(response => response.json())
            .then(data => {
                mostrarPeliculas(data);
            })
            .catch(error => {
                console.error('Error al cargar películas:', error);
                alert('Error al cargar películas');
            });
    }
    
    // Función para mostrar películas en la tabla
    function mostrarPeliculas(peliculas) {
        tablaPeliculas.innerHTML = '';
        
        if (peliculas.length === 0) {
            const tr = document.createElement('tr');
            tr.innerHTML = '<td colspan="4" class="text-center">No se encontraron películas</td>';
            tablaPeliculas.appendChild(tr);
            return;
        }
        
        peliculas.forEach(pelicula => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${pelicula.titulo}</td>
                <td>${pelicula.director || '-'}</td>
                <td>${pelicula.anio}</td>
                <td>${pelicula.genero || '-'}</td>
            `;
            tablaPeliculas.appendChild(tr);
        });
    }
    
    // Función para agregar una nueva película
    function agregarPelicula() {
        const titulo = document.getElementById('titulo').value;
        const director = document.getElementById('director').value;
        const anio = document.getElementById('anio').value;
        const genero = document.getElementById('genero').value;
        
        const nuevaPelicula = {
            titulo: titulo,
            director: director,
            anio: anio,
            genero: genero
        };
        
        fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(nuevaPelicula)
        })
        .then(response => response.json())
        .then(data => {
            // Limpiar el formulario
            formPelicula.reset();
            // Recargar la lista de películas
            cargarPeliculas();
            alert('Película agregada con éxito');
        })
        .catch(error => {
            console.error('Error al agregar película:', error);
            alert('Error al agregar película');
        });
    }
});