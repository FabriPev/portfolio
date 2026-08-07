const seedrandom = require('seedrandom');
const rng = seedrandom('1763519');
const total = 1000000;
const nums = [];

function getRandomInt32() {
  // Simula int32 con rango completo
  return Math.floor(rng() * 4294967296) - 2147483648;
}

// Generar 1 millón de números
for (let i = 0; i < total; i++) {
  nums.push(getRandomInt32());
}

// 1. Conteo positivos y negativos
let positivos = 0;
let negativos = 0;
for (const n of nums) {
  if (n > 0) positivos++;
  else if (n < 0) negativos++;
}

// 2. Cantidad de números cuyo resto %7 sea 0, 3, 5 o 6
let restoCounts = Array(7).fill(0);
for (const n of nums) {
  let r = ((n % 7) + 7) % 7; // asegurar que sea positivo
  restoCounts[r]++;
}
let cantResto_0_3_5_6 = restoCounts[0] + restoCounts[3] + restoCounts[5] + restoCounts[6];

// 3. Conteo por decena (0–9)
let decenas = Array(10).fill(0);
for (const n of nums) {
  const abs = Math.abs(n);
  const decena = Math.floor(abs / 10) % 10;
  decenas[decena]++;
}
const decenasFormatted = `{${decenas.join(',')}}`;

// 4. Mínimo y su posición (base 1)
let minVal = nums[0];
let minPos = 1;
for (let i = 1; i < nums.length; i++) {
  if (nums[i] < minVal) {
    minVal = nums[i];
    minPos = i + 1;
  }
}
const minFormatted = `${minVal}:${minPos}`;

// 5. Mismo signo que el anterior
let mismoSigno = 0;
for (let i = 1; i < nums.length; i++) {
  if ((nums[i] > 0 && nums[i - 1] > 0) || (nums[i] < 0 && nums[i - 1] < 0)) {
    mismoSigno++;
  }
}

// 6. Promedio de números de exactamente 6 dígitos
let suma6 = 0;
let cant6 = 0;
for (const n of nums) {
  const abs = Math.abs(n);
  if (abs >= 100000 && abs <= 999999) {
    suma6 += n;
    cant6++;
  }
}
const promedio6 = Math.round(suma6 / cant6);

// Resultados
console.log("Positivos:", positivos);
console.log("Negativos:", negativos);
console.log("Resto %7 = 0,3,5,6:", cantResto_0_3_5_6);
console.log("Decenas:", decenasFormatted);
console.log("Mínimo:posición:", minFormatted);
console.log("Mismo signo que anterior:", mismoSigno);
console.log("Promedio 6 dígitos:", promedio6);
