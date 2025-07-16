import dbm

from segunda_func import *
import random
import pickle
import os
import os.path


# La gerencia de una empresa de mudanzas mantiene un archivo en el cual cada registro contiene información sobre las
# mudanzas realizadas en un período. Por cada una de esas mudanzas se deben almacenar los datos siguientes:
# número identificación (un int), dirección de destino (otra cadena), un código entre 0 y 4 indicando el tipo vehículo
# a usar (0: camión, 1: camioneta, etc.), la tarifa válida por el traslado, y el tipo de carga que se transporta
# (un número entre 0 y 9). Se pide un programa completo con menú de opciones que para hacer lo siguiente:

# 1 Cargar registros en el archivo de mudanzas. Si el archivo no existía, crearlo. Si existía, preservar su contenido
# anterior.

# 2 Mostrar el archivo creado en el punto 1.

# 3 A partir del archivo, crear un arreglo de registros en el cual se copien los datos de todos los registros del archivo
# cuya tarifa sea mayor a la tarifa promedio de todo el arreglo. El arreglo debe crearse de forma que siempre quede
#  ordenado de menor a mayor, según el número de identificación de los clientes.

#  4 Mostrar el arreglo creado en el punto 3, a razón de un registro por línea en la pantalla.

#  Usando el archivo creado en el punto 1, determine la cantidad de mudanzas realizadas con cada posible tipo de
#  vehículo para cada uno de los posibles tipos de carga (o sea, 5 * 10 = 50 contadores en una matriz de conteo).
#  Muestre sólo los resultados diferentes de 0.

def menu():
    op = "Menu de opciones\n" \
         "1---Crear archivo\n" \
         "2---Mostar archivo\n" \
         "3---Crear arreglo\n" \
         "4---Mostrar arreglo\n" \
         "5---Matriz\n" \
         "6---Salir\n" \
         "Ingrese su opcion: "
    return op


def crear_archivo(n, nomb, ):
    direcciones = ("Cajamarca 1996", "Av velez Sarfield 2850", "Melincue 317", "Congreso 2017", "Av de Mayo 234",
                   "Viña del mar 3604", "Tafi 876")
    m = open(nomb, "ab")
    for i in range(n):
        identifiacion = random.randint(100, 900)
        direccion = random.choice(direcciones)
        codigo = random.randint(0, 4)
        tarifa = random.uniform(20000, 50000)

        tipo = random.randint(0, 9)
        mudanzas = Mudanza(identifiacion, direccion, codigo, tarifa, tipo)
        pickle.dump(mudanzas, m)

    m.close()


def mostrar_archivo(nomb):
    t = os.path.getsize(nomb)
    m = open(nomb, "rb")
    while m.tell() < t:
        mudanza = pickle.load(m)
        print(mudanza)

    m.close()


def add_in_order(nuevo, viejo):
    izq, der = 0, len(viejo) - 1
    pos = 0
    while izq <= der:
        mid = (izq + der) // 2
        if nuevo.identi == viejo[mid].identi:
            pos = mid
        if nuevo.identi < viejo[mid].identi:
            der = mid - 1
        else:
            izq = mid + 1

    if izq > der:
        pos = izq

    viejo[pos:pos] = [nuevo]


def crear_arreglo(v, nomb, bandera, prom):
    vector_temporal = []
    if not bandera:
        return "Realice el primer punto primero"

    m = open(nomb, "rb")

    t = os.path.getsize(nomb)

    while m.tell() < t:
        mudanza = pickle.load(m)
        add_in_order(mudanza, vector_temporal)
        n = len(vector_temporal)
        for i in range(n):
            total_tarifas = vector_temporal[i].tarifa
            prom = sacar_promedio(n, total_tarifas)

        if mudanza.tarifa > prom:
            add_in_order(mudanza, v)
    m.close()

    return prom


def mostar_arreglo(v, bandera):
    if not bandera:
        return "Realice el primer punto primero"

    n = len(v)

    for i in range(n):
        print(v[i])


def main():
    op = 0
    v = []
    punto_1 = False
    prom = 0
    nomb = ""

    while op != 6:
        op = int(input(menu()))
        if op == 1:
            nomb = input("Ingrese el nombre de archivo: ")
            n = int(input("Ingrese la cantidad de registros a cargar: "))
            n = validar_mayor_que(n, 0)
            crear_archivo(n, nomb)
            print("¡Archivo creado correctamente!")
            punto_1 = True
        if op == 2:
            mostrar_archivo(nomb)
        if op == 3:
            prom = crear_arreglo(v, nomb, punto_1, prom)
            print("Arreglo Creado")

        if op == 4:
            mostar_arreglo(v, punto_1)


if __name__ == '__main__':
    main()
