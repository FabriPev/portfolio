const btnCargarPersonas = document.getElementById("btnAgregar"); 
if (btnCargarPersonas) {
    btnCargarPersonas.addEventListener ("click", () => cargarPersonas());
}

const obtenerPersonas = async function () {
    const url = 'http://localhost:3001/api/personas';
    const respPersonas = await fetch(url);
    const personas = await respPersonas.json(); // Convierte la respuesta en formato json
    console.log('Personas-----> ', personas); // Muestra la lista de personas en la consola
    return personas; // Devuelve la lista de personas
    
}

const cargarPersonas = async function () {
    const personas = await obtenerPersonas();

    const listapersonas = document.getElementById("listaspersonas");
    if (listapersonas){
        let cuerpo = ''; // Inicializa el cuerpo de la tabla

        personas.forEach((persona) => {
            cuerpo += ` 
            <tr>
                <td>${persona.id}</td>
                <td>${persona.nombre}</td>
                <td>${persona.apellido}</td>
                <td>${persona.edad}</td>
            </tr>`; // Agrega una fila por cada persona
        })


        const tabla = `  
        <table>
            <thead>
                <tr>
                    <th>Id</th>
                    <th>Nombre</th>
                    <th>Apellido</th>
                    <th>Edad</th>
                </tr>
            </thead>
            <tbody>
                ${cuerpo}
            </tbody>
        </table>
        `

        listapersonas.innerHTML = tabla; // Inserta la tabla en el elemento con id listaspersonas
    }
}