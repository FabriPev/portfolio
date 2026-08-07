const fs = require('fs');

// Leer y parsear archivo JSON
const data = fs.readFileSync('personas.json', 'utf-8');
const personas = JSON.parse(data);

// 1. Promedio entero de edades
const promedioEdades = Math.floor(personas.reduce((sum, p) => sum + p.edad, 0) / personas.length);

// 2. Persona más joven
const personaJoven = personas.reduce((min, p) => (p.edad < min.edad ? p : min), personas[0]);
const nombreApellidoJoven = `${personaJoven.nombre} ${personaJoven.apellido}`;

// 3. Nombres con apellido GOMEZ ordenados alfabéticamente
const nombresGomez = personas
  .filter(p => p.apellido === "GOMEZ")
  .map(p => p.nombre)
  .sort()
  .join(", ");

// 4. Suma de edades: nombre longitud par y apellido impar
const sumaEdadesParImpar = personas
  .filter(p => p.nombre.length % 2 === 0 && p.apellido.length % 2 === 1)
  .reduce((sum, p) => sum + p.edad, 0);

// 5. JSON con mayores, menores, primeraMitad y segundaMitad
const estadisticas = {
  mayores: personas.filter(p => p.edad > 18).length,
  menores: personas.filter(p => p.edad <= 18).length,
  primeraMitad: personas.filter(p => /^[A-L]/i.test(p.apellido)).length,
  segundaMitad: personas.filter(p => /^[M-Z]/i.test(p.apellido)).length
};

// 6. Conteo por apellido
const apellidosObjetivo = ["CASTILLO", "DIAZ", "FERRER", "PINO", "ROMERO"];
const conteoApellidos = {};
for (const apellido of apellidosObjetivo) {
  conteoApellidos[apellido] = personas.filter(p => p.apellido === apellido).length;
}

// Resultados
console.log("Promedio entero de edades:", promedioEdades);
console.log("Persona más joven:", nombreApellidoJoven);
console.log("Nombres con apellido GOMEZ:", nombresGomez || "Ninguno");
console.log("Suma de edades (nombre par, apellido impar):", sumaEdadesParImpar);
console.log("Estadísticas (JSON):", JSON.stringify(estadisticas, null, 2));
console.log("Conteo por apellido (JSON):", JSON.stringify(conteoApellidos, null, 2));