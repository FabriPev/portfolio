# Guía de cambios 

## 1. Órden y filtros

Vamos a agregar órden y filtros al listado de personas. Comenzaremos por el backend y luego implementamos estos cambios en el frontend.

### 1.1. Primero especificamos algunas urls de las requests en el archivo .http que usamos para testear la API 

Vamos a considerar que podemos filtrar por nombre y apellido usando un patrón (no comparando por `=` sino por `like`). Además los filtros son opcionales: si no se especifican o se especifica uno solo tiene que omitir el/los filtros no especificados.

El órden puede ser por apellido o edad.

```http
###
GET http://localhost:{{port}}/api/personas?apellido=pe&nombre=ma&orden=apellido
###
GET http://localhost:{{port}}/api/personas?apellido=pe&orden=apellido
###
GET http://localhost:{{port}}/api/personas?orden=edad
```

### 1.2. Ahora modificamos el método correspondiente en el backend. Primero implementamos el órden.

```javascript
// ej: GET /api/personas
app.get('/api/personas', async (req, res) => {
    // Orden
    let campoOrden = req.query.orden || 'apellido';
    let expOrden = [[campoOrden, 'ASC']];

    // Parámetros
    let parameters = {order:expOrden}

    const personas = await Persona.findAll(parameters);
    res.json(personas);
})
```

### 1.3. Y luego agregamos los filtros en la expresión `where`.

Noten que tenemos que importar `Op` de `sequelize`.

```javascript
import {Op} from 'sequelize';
```

y luego completamos la lógica para aplicar los filtros y el órden en la query

```javascript
// ej: GET /api/personas
app.get('/api/personas', async (req, res) => {

    // Orden (si no se especifica ninguno, será apellido)
    let campoOrden = req.query.orden || 'apellido';
    let expOrden = [[campoOrden, 'ASC']];

    // filtros
    let filtroNombre = `%${req.query.nombre?req.query.nombre:''}%`;
    let filtroApellido = `%${req.query.apellido?req.query.apellido:''}%`;

    let expWhere = {
        nombre: {[Op.like]: filtroNombre},
        apellido: {[Op.like]: filtroApellido},
    };
    

    // Parámetros
    let parameters = {
        where: expWhere,
        order:expOrden
    }

    const personas = await Persona.findAll(parameters);
    res.json(personas);
})

```

Es importante leer la documentación de *Sequelize* para entender este código. Por ejemplo: [Model Querying - Basics](https://sequelize.org/docs/v6/core-concepts/model-querying-basics/)

### 1.4. Finalmente modificamos el frontend.

Agregamos lo siguiente en el `index.html` 

```html
...
        <div class="row">
            <div class="col">
                <label for="txtNombre">Nombre</label>
                <input type="text" name="txtNombre" id="txtNombre">
            </div>
            <div class="col">
                <label for="txtApellido">Apellido</label>
                <input type="text" name="txtApellido" id="txtApellido">
            </div>
            <div class="col">
                <label for="lstOrden">Orden</label>
                <select name="lstOrden" id="lstOrden">
                    <option value="apellido">Apellido</option>
                    <option value="edad">Edad</option>
                </select>
            </div>
            <div class="col">
                <button class="btn btn-success" id="btnCargarPersonas">Cargar Personas</button>
            </div>
        </div>
        ...

```

Y el código correspondiente en el archivo `js/index.js`

```javascript
const obtenerPersonas = async function(){
    const nombre = document.getElementById('txtNombre').value;
    const apellido = document.getElementById('txtApellido').value;
    const orden = document.getElementById('lstOrden').value;

    const url = `http://localhost:3001/api/personas?nombre=${nombre}&apellido=${apellido}&orden=${orden}`;
    const resPersonas = await fetch(url);
    const personas = await resPersonas.json();
    return personas;
}
```

## 2. Implementar la acción de eliminar una persona

Ya implementamos el backend oportunamente, por lo tanto, todo el trabajo lo tenemos que hacer en el backend

### 2.1. Inicialmente agregamos un botón a cada fila de la tabla.

Para invocar la acción de eliminar pasando el id como parámetro en la función que renderiza la tabla agregamos:


```javascript
const cargarPersonas = async function(){

    const personas = await obtenerPersonas();
    
    const listaPersonas = document.getElementById('listaPersonas');
    if(listaPersonas){
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

        listaPersonas.innerHTML= tabla;
    }
}
```

### 2.2. Agregamos la función `eliminarPersona()`.

```javascript
const eliminarPersona = async function (id) {
    if (window.confirm(`¿Desea eliminar esta persona?`)) {
        const url = `http://localhost:3001/api/personas/${id}`;
        const resPersonas = await fetch(url, { method: 'DELETE' });
        await cargarPersonas();
    }
}
```
