const btnCargarPersonas = document.getElementById('btnCargarPersonas');
if (btnCargarPersonas) {
    btnCargarPersonas.addEventListener('click', () => cargarPersonas());
}

const obtenerPersonas = async function () {
    const nombre = document.getElementById('txtNombre').value;
    const apellido = document.getElementById('txtApellido').value;
    const orden = document.getElementById('lstOrden').value;

    const url = `http://localhost:3001/api/personas?nombre=${nombre}&apellido=${apellido}&orden=${orden}`;
    const resPersonas = await fetch(url);
    const personas = await resPersonas.json();
    return personas;
}

const eliminarPersona = async function (id) {
    if (window.confirm(`¿Desea eliminar esta persona?`)) {
        const url = `http://localhost:3001/api/personas/${id}`;
        const resPersonas = await fetch(url, { method: 'DELETE' });
        await cargarPersonas();
    }
}

const cargarPersonas = async function () {

    const personas = await obtenerPersonas();

    const listaPersonas = document.getElementById('listaPersonas');
    if (listaPersonas) {
        let cuerpo = ''

        personas.forEach(p => {
            let botonEliminar = `<td><button class="btn btn-danger" onClick="eliminarPersona(${p.id})">Eliminar</button></td>`
            cuerpo += `<tr><td>${p.nombre}</td><td>${p.apellido}</td><td>${p.edad}</td>${botonEliminar}</tr>`
        })


        const tabla = `
            <table class="table">
                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>Apellido</th>
                        <th>Edad</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    ${cuerpo}
                </tbody>
            </table>
        `

        listaPersonas.innerHTML = tabla;
    }
}