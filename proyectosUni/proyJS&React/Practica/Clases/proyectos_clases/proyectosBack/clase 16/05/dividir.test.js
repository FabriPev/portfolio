import { dividir } from "./calculadora";
test("divido 1 entre 2 y tiene que dar 0,5", 
    () => {
        const resultado = dividir(1, 2);
        expect(resultado).toBe(0.5);
    }
);

test("divido 1 entre 0 y tiene que dar NaN", 
    () => {
        const resultado = dividir(1, 0);
        expect(resultado).toBe(NaN);
    }
);
