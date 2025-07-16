from parcial3_1 import *
import random


def menu():
    cad = "Menu de opciones\n" \
          "========================\n" \
          "1----- Cargar el arreglo pedido con los datos de los n trabajos\n" \
          "2----- Mostrar todos los datos de todos los trabajos cuya cantidad de personal sea mayor a 3\n" \
          "3----- Determinar y mostrar la cantidad de trabajos que se ofrecen de cada tipo posible\n" \
          "4----- Mostrar los datos de todos los trabajos cuyo importe a cobrar sea mayor al importe promedio de todos los trabajos del arreglo\n" \
          "5-----Determinar si existe un trabajo cuyo número de identificación sea igual a num y que sea del tipo t\n" \
          "0-----Salir\n" \
          "Elija su opcion: "
    return int(input(cad))


def cargar_vector(vector, n):
    lugar = "Cordoba", "Santa Fe", "Mendoza", "La rioja", "Salta"
    for i in range(n):
        num_iden = f"{random.randint(1,999999), 0 > 6}"
        descrip = random.choice(lugar)
        tipo = random.randint(0, 19)
        importe = round(random.uniform(2000, 10000), 2)
        personal = random.randint(1, 150)
        trabajo = Trabajos(num_iden, descrip, tipo, importe, personal)
        vector.append(trabajo)


def principal():
    op = -1
    vector = []
    while op != 0:
        op = menu()
        if op == 1:
            n = validar_mayor_a(0, "Ingrese la cantidad de trabajos a cargar: ")
            cargar_vector(vector, n)
        if len(vector) > 0:
            if op == 2:
                suma = 0
                ordenar(vector)
                for trabajo in vector:
                    if trabajo.personal > 3:
                        print(trabajo)
                        suma += trabajo.importe
                print("La suma de los importes es: ")
            if op == 3:
                cont = [0] * 20
                for i in range(len(vector)):
                    pos = vector[i].tipo
                    cont[pos] += 1
                for i in range(len(vector)):
                    if cont[i] > 0:
                        print(str(cont[i]) + ", ", end=" ")
            if op == 4:
                pass
            if op == 5:
                pass
        else:
            print("Primero debe cargar los trabajos ")


if __name__ == '__main__':
    principal()
