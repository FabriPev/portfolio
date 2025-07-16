from pract5ica_func import *
import random
import pickle
import os.path


def menu():
    op = "Menu de opciones\n" \
         "1-----Cargar arreglo\n" \
         "2-----Mostrar arreglo\n" \
         "3-----Buscar arreglo\n" \
         "4-----Crear archivo\n" \
         "5-----Mostar archivo\n" \
         "6-----Generar  y mostrar matriz\n" \
         "7-----Salir\n" \
         "Ingrese su opcion: "

    return int(input(op))


def cargar_arreglo(vector, n):
    descrip = ("caso corto", "caso largo", "caso de duracion media", "caso flash", "caso extra largo")
    for i in range(n):
        iden = random.randint(1, 1000)
        desc = random.choice(descrip)
        monto = random.randint(10000, 200000)
        tipo = random.randint(0, 19)
        tribunal = random.randint(1, 10)
        casos = Caso(iden, desc, monto, tipo, tribunal)
        add_in_order(vector, casos)


def mostrar_arreglo(vector, t):
    n = len(vector)
    for i in range(n):
        if vector[i].tribunal != t:
            print(vector[i])


def buscar_arreglo(des, vector):
    n = len(vector)
    printeo = False
    for i in range(n):
        if vector[i].descrip == des:
            print(vector[i])
            printeo = True
            break
    if not printeo:
        print("No hay un caso con ese descripcion")


def crear_archivo(k, vector):
    x = int(input("Ingrese el maximo para mostrar"))
    x = validar_mayor_que(x, 0)
    n = len(vector)
    m = open(k, "wb")
    for i in range(n):
        if vector[i].tipo == 3 or vector[i].tipo == 4:
            if vector[i].monto < x:
                pickle.dump(vector[i], m)
    m.close()


def mostrar_archivo(k, vector):
    taman = os.path.getsize(k)
    cont = 0
    m = open(k, "rb")
    while m.tell() < taman:
        caso = pickle.load(m)
        print(caso)
        cont += 1
    print("Se han mostrado, ", cont, "casos")


def generar_matriz(vector):
    mat = [[0] * 20 for i in range(10)]
    n = len(vector)
    for i in range(n):
        c = vector[i].tipo
        f = vector[i].tribunal
        mat[f-1][c] += vector[i].monto

    for f in range(10):
        for c in range(20):
            if mat[f][c] > 0:
                print("En el tribunal numero, ", f+1, "y caso tipo", c, "se acumulo un total de: $", mat[f][c])


def prinicapl():
    op = -1
    vector = []
    k = ""
    while op != 7:
        op = menu()
        if op == 1:
            n = int(input("Cuantos arreglos desea cargar: "))
            n = validar_mayor_que(n, 0)
            cargar_arreglo(vector, n)
        elif len(vector) > 0:
            if op == 2:
                t = int(input("Ingrese un valor de tribunal a excluir: "))
                t = validar_entre(t, 1, 10)
                mostrar_arreglo(vector, t)
            elif op == 3:
                des = input("Ingrese la descripcion del caso: ")
                des = des.lower()
                buscar_arreglo(des, vector)
            elif op == 4:
                k = input("Ingrese el nombre del archivo deseado: ")
                crear_archivo(k, vector)
            elif op == 5:
                if os.path.exists(k):
                    mostrar_archivo(k, vector)
                else:
                    print("Archvio no existente, primero realize el punto 4")
            elif op == 6:
                generar_matriz(vector)


if __name__ == '__main__':
    prinicapl()
