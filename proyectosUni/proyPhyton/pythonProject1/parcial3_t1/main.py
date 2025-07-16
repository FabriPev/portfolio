from registros import *
import random


def menu():
    cad = "Menu de opciones\n" \
          "1------ Cargar el arreglo pedido\n" \
          "2------ Punto 2\n" \
          "3------ Punto 3\n" \
          "4------ Punto 4\n" \
          "5------ Salir\n" \
          "Ingrese su opcion: "
    return int(input(cad))


def cargar_vector(vector, n):
    nombres = "Pedro", "Juan", "Camila", "Lucia", "Santiago", "Valentina"
    apellido = "Rodriguez", "Sanchez", "Gutierrez", "Martinez"
    for i in range(n):
        iden = i + 1
        nombre = random.choice(nombres)
        apellido_clien = random.choice(apellido)
        tipo = random.randint(0, 19)
        monto = round(random.uniform(4000, 8000), 2)
        paseo = Paseos(iden, nombre, apellido_clien, tipo, monto)
        vector.append(paseo)


def sumar_tot(vector):
    tot = 0
    for i in range(len(vector)):
        tot += vector.monto
    return tot


def carga_por_tipo(vector):
    cont = [0] * 20


def principal():
    op = -1
    vector = []
    while op != 5:
        op = menu()
        if op == 1:
            cant = mayor_a(0, "Ingrese la cantidad de paseos a cargar: ")
            cargar_vector(vector, cant)
        if len(vector) > 0:
            if op == 2:
                write(vector)
            elif op == 3:
                pass
            elif op == 4:
                pass
        else:
            print("Primero cargue los arreglos")


if __name__ == '__main__':
    principal()
