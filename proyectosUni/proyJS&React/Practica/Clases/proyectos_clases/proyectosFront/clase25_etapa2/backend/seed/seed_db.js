import seedPersonas from './seed_personas.js'
import seedPeliculas from './seed_peliculas.js'
await seedPersonas.inicializarDesdeJSON('./seed/personas.json');
await seedPeliculas.inicializarDesdeJSON('./seed/peliculas.json');