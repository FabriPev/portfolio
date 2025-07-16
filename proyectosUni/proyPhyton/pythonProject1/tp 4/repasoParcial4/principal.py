import random
from registro import *
import pickle
import os.path

def add_in_order(gastos, reg):
    n = len(gastos)
    izq, der = 0, n-1
    pos = n
    while izq <= der:
        c = (izq + der) // 2
        if gastos[c].descripcion == reg.descripcion:
            pos = c
            break
        if gastos[c].descripcion > reg.descripcion:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    gastos[pos:pos] = [reg]


def cargar_vector(gastos, n):
    descripciones = ("Agua", "Luz", "Rentas", "Alquiler", "Limpieza", "Gas")
    for i in range(n):
        cod = i + 1
        desc = random.choice(descripciones)
        mes = random.randint(1, 12)
        suc = random.randint(0, 2)
        imp = random.uniform(1000, 40000)
        reg = Gasto(cod, desc, mes, suc, imp)
        add_in_order(gastos, reg)


def mostrar_vector(gastos):
    for i in range(len(gastos)):
        print(gastos[i])


def generar_archivo(v, gastos):
    m = open("gastos.dat", "wb")
    for i in range(len(gastos)):
        if gastos[i].importe > v:
            pickle.dump(gastos[i], m)
    m.close()


def mostrar_archivo():
    nom_arch = "gastos.dat"
    if not os.path.exists(nom_arch):
        print("El archivo no existe!")
        return
    m = open(nom_arch, "rb")
    tam = os.path.getsize(nom_arch)
    while m.tell() < tam:
        gasto = pickle.load(m)
        write(gasto)
    m.close()


def buscar_codigo(gastos, c):
    for i in range(len(gastos)):
        if gastos[i].codigo == c:
            return i
    return -1



def generar_matriz():
    arch = "gastos.dat"
    if not os.path.exists(arch):
        print("Archivo no existe!")
        return None
    mat = [[0] * 12 for i in range(3)]
    m = open(arch, "rb")
    tam = os.path.getsize(arch)
    while m.tell() < tam:
        reg = pickle.load(m)
        fil = reg.sucursal
        col = reg.mes - 1
        mat[fil][col] += reg.importe
    m.close()
    return mat


def mostrar_matriz(mat):
    for i in range(len(mat)): #filas: 3
        for j in range(len(mat[i])): #columnas: 12
            if mat[i][j] > 0:
                print("Sucursal", i, "- Mes", j+1, "- $", mat[i][j])


def totalizar_mes(mes, mat):
    acu = 0
    for i in range(len(mat)):
        acu += mat[i][mes-1]
    print("Total acumulado del mes:$", acu)


def totalizar_sucursal(suc, mat):
    acu = 0
    for j in range(len(mat[0])):
        acu += mat[suc][j]
    print("Total acumulado de la sucursal:$", acu)


def principal():
    gastos = []
    op = 1
    band_6 = False
    while op != 0:
        print("Menú de opciones")
        print("1-Cargar vector")
        print("2-Mostrar vector")
        print("3-Generar Archivo")
        print("4-Mostrar Archivo")
        print("5-Buscar")
        print("6-Matriz de acumulación")
        print("7-Totalizar mes")
        print("8-Totalizar sucursal")
        print("0-Salir")
        op = int(input("Ingrese la opción que desea: "))
        if op == 1:
            n = int(input("Ingrese la cantidad de gastos a cargar: "))
            cargar_vector(gastos, n)
        elif len(gastos) == 0:
            print("Primero debe cargar el vector")
        elif op == 2:
            mostrar_vector(gastos)
        elif op == 3:
            v = float(input("Ingrese el valor a superar para generar el archivo: $"))
            generar_archivo(v, gastos)
        elif op == 4:
            mostrar_archivo()
        elif op == 5:
            c = int(input("Ingrese el código a buscar: "))
            pos = buscar_codigo(gastos, c)
            if pos == -1:
                print("El código no se encuentra en el vector")
            else:
                print("Gasto encontrado!!!")
                print(gastos[pos])
        elif op == 6:
            mat = generar_matriz()
            if mat:
                mostrar_matriz(mat)
                band_6 = True
        elif op == 7:
            if band_6:
                mes = int(input("Ingrese el mes a totalizar: "))
                totalizar_mes(mes, mat)
            else:
                print("Primero debe crear la matriz")
        elif op == 8:
            if band_6:
                suc = int(input("Ingrese una sucursal a totalizar: "))
                totalizar_sucursal(suc, mat)
            else:
                print("Primero debe crear la matriz")


if __name__ == '__main__':
    principal()
