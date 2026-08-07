import { use, useEffect } from "react";
import { useState } from "react";


function Componente1({nombre, apellido}) {

    //Generar un numero aleatorio entre 0 y 100
    const Aleatorio = Math.floor(Math.random() * 100);
    const [numero, setNumero] = useState(Aleatorio);
    useEffect( () => { 
        console.log(`valor ${numero} cambiado`);
    }, [numero, nombre, apellido]);  // Se ejecuta cada vez que cambia el numero, nombre o apellido
    useEffect( () => { 
        console.log(`inicia el componente ${nombre}`);
    }, []); // Se ejecuta una sola vez al cargar el componente
    useEffect( () => { 
        console.log(`valor ${numero}`);
    },);

    return (
        <div>
            <h1>{nombre} {apellido ?? "sin apellido"} : {numero}</h1>
            <p>Este es el primer Componente</p>
            <button onClick={() => setNumero(numero + 1)}>+</button>
            <button onClick={() => setNumero(0)}>0</button>
            <button onClick={() => setNumero(numero - 1)}>-</button>
        </div>
    )
}

export default Componente1;