from cuarto_funciones import *
import random
import os.path
import os
import pickle


def menu():
    op = "Menu de opciones\n" \
         "1----Generar arreglo\n" \
         "2----Mostrar arreglo\n" \
         "3----Listado ordenado por número de identificación\n" \
         "4----Monto acumulado que se cobró durante cada una de las 24 horas del día en las diferentes casillas de peaje\n" \
         "5----Genere un archivo binario\n" \
         "6----Muestre el archivo\n" \
         "7----Informar si se le ha cobrado un peaje a un auto cuya patente es un valor p, a una determinada hora h\n" \
         "8----Tome la cadena retornada en el punto 7 anterior, y determine cuántas palabras de esa cadena contienen al " \
         "menos una letra mayúscula\n" \
         "9----Salir\n" \
         "Ingrese su opcion: "

    return op


def crear_arreglo(n, vector):
    accesos = (
        "Autopista Carlos Paz.", "Córdoba acceso norte.", "Córdoba acceso oeste.", "Autopista Camino Alta Gracia."
        , "Autopista Camino al Cuadrado", "Córdoba acceso este.")
    paten = ("LVO", "UPO", "KHE", "LPR", "RET", "TYU", "KYS")
    for i in range(n):
        identificacion = random.randint(1, 100)
        puesto = random.choice(accesos)
        monto = random.uniform(300, 1000)
        patente = random.choice(paten) + str(random.randint(100, 999))
        hora = random.randint(0, 23)
        cobros = Cobro(identificacion, puesto, monto, patente, hora)
        vector.append(cobros)


def mostrar_arreglo(vec):
    l = len(vec)
    for i in range(l):
        print(vec[i])


def add_in_order(nuevo, viejo):
    izq, der = 0, len(viejo) - 1
    pos = 0
    while izq <= der:
        med = (izq + der) // 2
        if viejo[med].iden == nuevo.inden:
            pos = med
        if nuevo.iden < viejo[med].iden:
            der = med - 1
        else:
            izq = med + 1
    if izq > der:
        pos = izq

    viejo[pos:pos] = [nuevo]


def crear_arreglo_ord(vec, m, vec_sec):
    cont = 0

    z = len(vec)

    for i in range(z):
        if vec[i].monto < m:
            add_in_order(vec, vec_sec)
            cont += 1
    print("Se han cargado ", cont, "de vectores")
    mostrar_arreglo(vec_sec)


def crear_matriz(vec):
    mat = [[0] * 24 for i in range(6)]


def principal():
    op = 0
    vec = []
    vec_sec = []
    while op != 9:
        op = int(input(menu()))
        if op == 1:
            n = int(input("Cuantos registros desea crear: "))
            validar_mayor_que(n, 0)
            crear_arreglo(n, vec)
        elif op == 2:
            if not len(vec) == 0:
                mostrar_arreglo(vec)
            else:
                print("¡ERROR! Realice el punto 1 primero!")
        elif op == 3:
            if not len(vec) == 0:
                m = int(input("Ingrese el valor minimo de monto para mostrar"))
                validar_entre(m, 300, 1000)
                crear_arreglo_ord(vec, m, vec_sec)
            else:
                print("¡ERROR! Realice el punto 1 primero!")
        elif op == 4:
            if not len(vec) == 0:
                crear_matriz(vec)
            else:
                print("¡ERROR! Realice el punto 1 primero!")


if __name__ == '__main__':
    principal()
