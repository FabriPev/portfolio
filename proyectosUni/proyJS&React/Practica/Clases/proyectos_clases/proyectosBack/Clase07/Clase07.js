class Persona {
    constructor(nombre, apellido, edad){
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
    }

nombre_completo(){
    return this.nombre + " " + this.apellido;}

mayor_edad(){
    return this.edad >= 18;
}

}

let personita1 = new Persona("Constanza" , "Moyano Doval", 19);
console.log(personita1.nombre_completo())
personita1.edad ++

///notacion literal :





const texto = '{ "nombre" : "Lapiz negro", "precio" : 45, "stock" : 500 }';

const art1 = JSON.parse(texto)
console.dir(personita1);
console.log  (art1.nombre)
art1.stock -= 10;
art1.precio *= 1.05;
console.dir(art1);


console.dir(art1)
    art1.precio *= 1.1;
const texto2 = JSON.stringify(art1);

const numeros = [1, 3];
numeros.push(5);


for(let i = 0; i <= numeros.length; i++){
    console.log(numeros[i])
}
const numeros2 = [];
numeros2.push(5);
for (let x of numeros2){console.log(x)}

const puntos =[{x:0, y:0}, {x:0, y:4}, {x:2, y:5}]
for (let p of puntos){
    
}