import random
import pickle
import os
import os.path
from tercer_funciones import *


# Un complejo de cines quiere realizar un análisis de las ventas del último mes sobre las películas que expuso
# en la cartelera, por cada Entrada vendida se conoce número, nombre de la película,
# tipo de proyección (1 - Normal, 2 - 3D, 3 - IMAX, 4 - IMAX 3D),
# clasificación de INCAA (0 - ATP, 1 - M13, 2 - M16, 3 - M18), precio de la entrada y día de venta (valor de 1 a 31)

# La empresa tiene el detalle de las entradas vendidas guardadas en un archivo  "tickets.dat",
# el cual usted debe cargarlo en un vector en forma ordenada por el número de la entrada, a partir del
# vector mediante un menú de opciones:

def menu():
    op = "Menu de opciones\n" \
         "1---Listar todas las entradas vendidas en un día X ingresado por teclado.\n" \
         "2---Determinar el total vendido para cada tipo de proyección y clasificación de la película (matriz de acumulación)" \
         ".\n" \
         "3---Grabar en un archivo de texto el nombre de la película y la clasificación de todas aquellas ventas para " \
         "un tipo de proyección X ingresada por teclado.\n" \
         "4---Determinar cuál es el tipo de proyección que más recaudó en el mes.\n" \
         "5---Grabar en un segundo archivo las ventas de entradas para un día X y una clasificación Y ambos ingresados por teclado.\n" \
         "6---Salir\n" \
         "Ingrese su opcion: "
    return op


def add_in_order(viejo, nuevo):
    izq, der = 0, len(viejo) - 1
    pos = 0
    while izq < der:
        med = (izq + der) // 2
        if viejo[med].numero == nuevo.numero:
            pos = med
        if viejo[med].numero < nuevo.numero:
            izq = med + 1
        else:
            der = med - 1
    if der < izq:
        pos = izq

    viejo[pos:pos] = [nuevo]


def formar_vec(vec_prin, asac):
    if not os.path.exists(asac):
        return "No hay archivo con información de los tickets"

    m = open(asac, "rb")
    t = os.path.getsize(asac)

    while m.tell() < t:
        ticket = pickle.load(m)
        add_in_order(vec_prin, ticket)

    m.close()


def mostrar_por_dia(n, vec_prin):
    j = len(vec_prin)
    for i in range(j):
        if vec_prin[i].dia == n:
            print(vec_prin[i])


def generar_matriz(vec_prin):
    pass


def principal():
    op = 0
    vec_prin = []
    asac = "tickets.dat"
    formar_vec(vec_prin, asac)
    while op != 6:
        op = int(input(menu()))
        if op == 1:
            n = "Ingrese el dia para buscar: "
            validar_entre(n, 1, 31)
            mostrar_por_dia(n, vec_prin)
        if op == 2:
            generar_matriz(vec_prin)


if __name__ == '__main__':
    principal()
