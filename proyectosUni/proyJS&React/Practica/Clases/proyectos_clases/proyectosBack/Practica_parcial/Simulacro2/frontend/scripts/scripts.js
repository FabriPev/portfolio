document.addEventListener('DOMContentLoaded', () => {
    const API_URL = 'http://localhost:3000/api/libros';
    const btnBuscar = document.getElementById("botonBuscar");
    const tablaLibros = document.querySelector("#tablaLibros tbody");

    mostrarLibros(tablaLibros, API_URL);

    btnBuscar.addEventListener('click', () => {
        const Titulo = document.getElementById('tituloBuscar').value;
        mostrarLibros(tablaLibros, API_URL, Titulo);
    });

    function mostrarLibros(tablaLibros, API_URL, Titulo = '') {
        let url = API_URL;
        if (Titulo) {
            const params = new URLSearchParams({ search: Titulo });
            url += `?${params.toString()}`;
        }

        fetch(url)
            .then(res => res.json())
            .then(libros => {
                tablaLibros.innerHTML = '';
                libros.forEach(L => {
                    const fila = document.createElement('tr');
                    fila.innerHTML = `
                        <td>${L.IdLibro}</td>
                        <td>${L.Titulo}</td>
                        <td>${L.Autor}</td>
                        <td>${L.AnioPublicacion}</td>
                        <td>
                            <button class="btn btn-danger btn-sm eliminar-btn" data-id="${L.IdLibro}">Eliminar</button>
                        </td>
                    `;
                    tablaLibros.appendChild(fila);
                });

            
                document.querySelectorAll('.eliminar-btn').forEach(boton => {
                    boton.addEventListener('click', () => {
                        const id = boton.dataset.id;
                        const fila = boton.closest('tr');
                        if (confirm('¿Estás seguro de que deseas eliminar este libro?')) {
                            fetch(`${API_URL}/${id}`, { method: 'DELETE' })
                                .then(response => {
                                    if (response.ok) 
                                    {mostrarLibros(tablaLibros, API_URL, document.getElementById('tituloBuscar').value)}  
                                    else alert("Error al eliminar.");
                                });
                        }
                    });
                });
            });
    }
});
