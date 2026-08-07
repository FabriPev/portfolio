const seedrandom = require('seedrandom');

const rng = seedrandom(1763519);

let numeros = [];
for (let i = 0; i<1000000; i++) {
    numeros.push(rng.int32());
}

function positivos_negativos(numeros) {
    let positivos = 0;
    let negativos = 0;
    for (n of numeros) {
        if (n > 0) {
            positivos++;
        } else if (n < 0) {
            negativos++;
        }
}
    return [positivos, negativos];
}

function resto (numeros){
    let resto = 0;
    for (let i = 0; i <= numeros.length; i++) {
        let queda = numeros[i] % 7;
        if (queda === 0 || queda === 3 || queda === 5 || queda === 6) {
            resto++;
        } 
    }
    return resto;
}

function menor_posicion (numeros){
    let menor = null;
    let posicion = 0;
    for (let i = 0; i < numeros.length; i++) {
        if (numeros[i] < menor || menor == null) {
            menor = numeros[i];
            posicion = i + 1;
        }
    }
    return [menor, posicion];
}
function leer_decena(numeros){
    let contadores = new Array(10).fill(0);
    for (let i = 0; i < numeros.length; i++) {
        let numero = Math.abs(numeros[i]);
        numero = Math.floor(numero/ 10);
        let decena = numero % 10;
        
        contadores[decena]++;
    }
    return contadores;
}

function leer_mismo_signo(numeros){
    let ultimo = null;
    let cantidad_mismo_signo = 0
    for (let i = 0; i < numeros.length; i++) {
        if (numeros[i] * ultimo > 0) {
            cantidad_mismo_signo++;
        }
        ultimo = numeros[i];
       
    }
    return cantidad_mismo_signo;
}

function promedio(numeros){
    let suma = 0;
    let cantidad = 0;
    
    for (let i = 0; i < numeros.length; i++) {
        let numero = Math.abs(numeros[i]);
        if (String(numero).length === 6) {
            suma += numeros[i];
            cantidad++;
        }
}
    if (cantidad === 0) {
        return 0;
    }
    const promedio = suma / cantidad;
    return (Math.round(promedio));
    ;
}




const [numeros_positivos, numeros_negativos] = positivos_negativos(numeros);
const resto_numeros = resto(numeros);
const [menor, posicion] = menor_posicion(numeros);

const decenas = leer_decena(numeros);
const numeros_mismo_signo = leer_mismo_signo(numeros);
const promedio_numeros = promedio(numeros);



console .log (`Numeros positivos: ${numeros_positivos}`);

console.log(`Numeros negativos: ${numeros_negativos}`);
console.log(`Numeros totales: ${numeros.length}`);
console.log(`Numeros que cumplen la condicion de resto: ${resto_numeros}`);
console.log(`Array de veces en las decenas ${decenas}`);
console.log(`Menor numero: ${menor}, Posicion del menor numero: ${posicion}`);
console.log(`Cantidad de numeros con el mismo signo: ${numeros_mismo_signo}`);
console.log(`Promedio de numeros con 6 digitos: ${promedio_numeros}`);