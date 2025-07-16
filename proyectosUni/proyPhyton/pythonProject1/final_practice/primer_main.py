import pickle
import os.path
import os
import random
from primer_funciones import *


def menu():
    op = "Menu de opciones\n" \
         "1---Generar registro y guardar en archivo\n" \
         "2---Mostrar archivo\n" \
         "3---Crear arreglo\n" \
         "4---Buscar inquilino\n" \
         "5---Matriz\n" \
         "6---Salir\n" \
         "Seleccione su opcion: "
    return op


def generar_archivo(nombre, n):
    nombres = ("Juan", "Pedro", "Daniela", "Camilia", "Pilar", "Tomas")
    m = open(nombre, "wb")
    for i in range(n):
        name = random.choice(nombres)
        iden = random.randint(1, 100)
        piso = random.randint(1, 12)
        codigo = random.randint(0, 4)
        monto = random.uniform(10000, 30000)
        departamentos = Departamento(iden, name, piso, codigo, monto)
        pickle.dump(departamentos, m)
    m.close()


def mostrar_archivo(nomb):
    if not os.path.exists(nomb):
        return "El nombre de archivo no existe vuelva al punto 1"

    m = open(nomb, "rb")
    t = os.path.getsize(nomb)

    while m.tell() < t:
        departamentos = pickle.load(m)
        print(departamentos)
    m.close()


def validad_mayor_que(n, numero):
    while numero >= n:
        print("Error ingrese un numero mayor que", numero)
        n = int(input("Ingrese su nuevo valor: "))
    else:
        return n


def add_in_order(viejo, nuevo):
    izq, der = 0, len(viejo) - 1
    pos = len(viejo)
    while izq <= der:
        med = (izq + der) // 2
        if viejo[med].identificacion == nuevo.identificacion:
            pos = med
        if viejo[med].identificacion > nuevo.identificacion:
            der = med - 1
        else:
            izq = med + 1
    if izq > der:
        pos = izq

    viejo[pos:pos] = [nuevo]


def crear_arreglo(v, nomb):
    if not os.path.exists(nomb):
        return "El archivo no existe vuelva al punto 1"
    m = open(nomb, "rb")
    t = os.path.getsize(nomb)
    while m.tell() < t:
        departamentos = pickle.load(m)
        add_in_order(v, departamentos)
    m.close()


def mostrar_arreglo(v):
    if len(v) == 0:
        print("Realice el punto 3 primero")
        return
    for i in range(len(v)):
        print(v[i])


def busqueda_secuencial(v):
    vector_nuevo = []
    nombre = input("Ingrese el nombre del inquilino a buscar: ")
    for i in range(len(v)):
        if v[i].identificacion == nombre:
            vector_nuevo = v[i]
            print(vector_nuevo)


def generar_matriz(v):
    martiz = [[0] * 12 for i in range(5)]


def main():
    op = 0
    v = []
    nomb = ""
    punto_1 = False
    while op != 6:
        op = int(input(menu()))
        if op == 1:
            n = int(input("Ingrese la cantidad de registro a generar: "))
            validad_mayor_que(n, 0)
            nomb = input("Seleccione un nombre para el archivo: ")
            generar_archivo(nomb, n)
            print("Archivo generado con exito")
            punto_1 = True
        if punto_1:
            if op == 2:
                mostrar_archivo(nomb)
            if op == 3:
                crear_arreglo(v, nomb)
                print("Arreglo creado con exito")
            if op == 4:
                busqueda_secuencial(v)
            if op == 5:
                generar_matriz(v)


if __name__ == '__main__':
    main()
