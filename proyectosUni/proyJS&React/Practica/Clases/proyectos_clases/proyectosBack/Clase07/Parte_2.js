///import personas from "./personas.json" with { type: "json"};

console.dir(personas)
//Mostrar nombre y apellido de las personas con edad > 30
const personas = require ("./personas.json")
for(const cadaPersona of personas){
    if (cadaPersona.edad > 30)
        console.log(`${cadaPersona.nombre} ${cadaPersona.apellido} ${cadaPersona.edad}`)
}
