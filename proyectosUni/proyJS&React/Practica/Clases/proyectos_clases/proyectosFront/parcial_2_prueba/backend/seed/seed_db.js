import seedPersonas from './seed_personas.js'
import seedCiudades from './seed_ciudades.js'
await seedPersonas.inicializarDesdeJSON('./seed/personas.json');
await seedCiudades.inicializarDesdeJSON('./seed/ciudades.json');