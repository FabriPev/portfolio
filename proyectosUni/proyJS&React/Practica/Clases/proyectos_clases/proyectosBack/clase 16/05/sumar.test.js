import { sumar } from "./calculadora";


test("sumo 1+1 y tiene que dar 2", 
    () => {
        const resultado = sumar(1, 1);
        expect(resultado).toBe(2);
    }
);
