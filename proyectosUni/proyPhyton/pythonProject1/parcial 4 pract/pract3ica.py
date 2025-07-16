from pract3ica_func import *
import random
import os.path
import pickle


def menu():
    op = "Menu de opciones\n" \
         "1----Cargar arreglo\n" \
         "2----Mostrar arreglo\n" \
         "3----Matriz para contar cuántas operaciones de cada tipo se hicieron en cada posible zona\n" \
         "4----Generar archivo\n" \
         "5----Mostar archivo\n" \
         "6----Salir\n" \
         "Ingrese su opcion: "

    return int(input(op))


def validar_mayor_que(min, n):
    while n <= min:
        print("Numero no valido, ingrese un numero mayor a: ", n)
        n = int(input("Ingrese su nuevo numero: "))
    return n


def add_in_order(vector, servicios):
    izq, der = 0, len(vector) - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if servicios.iden == vector[c].iden:
            pos = c
            break
        if servicios.iden > vector[c].iden:
            izq = c + 1
        else:
            der = c - 1
    if der < izq:
        pos = izq

    vector[pos:pos] = [servicios]


def cargar_arreglo(vector, n, cont):
    descrip = ("Nuevos campos", "Campos a reutilizar", "Campos con mucho degaste", "Campos en recuperacion")
    for i in range(n):
        iden = random.randint(1, 1000)
        descripciones = random.choice(descrip)
        monto = round(random.uniform(10000, 100000), 2)
        cont += monto
        tipo = random.randint(1, 15)
        zona = random.randint(0, 19)
        servicios = Servicio(iden, descripciones, monto, tipo, zona)
        add_in_order(vector, servicios)
    return cont


def mostrar(vector):
    for i in range(len(vector)):
        print(vector[i])


def hacer_matriz(vector):
    a = int(input("Ingrese el minimo del contador para mostrar: "))
    a = validar_mayor_que(0, a)
    b = int(input("Ingrese el maximo del contador para mostrar: "))
    b = validar_mayor_que(a, b)

    mat = [[0] * 20 for i in range(15)]
    n = len(vector)
    for i in range(n):
        f = vector[i].tipo
        c = vector[i].zona
        mat[f][c-1] += 1

    for f in range(15):
        for c in range(20):
            if a <= mat[f][c] <= b:
                print("En la ciudad Nº: ", c+1, "y tipo de opereacion Nº: ", f, "hubo un total de ", mat[f][c],
                      "operaciones")


def crear_archivo(k, vector, prom):
    cont = 0
    n = len(vector)
    m = open(k, "wb")
    for i in range(n):
        if vector[i].importe > prom:
            pickle.dump(vector[i], m)
            cont += 1
    print("Se han grabado", cont, "operaciones")
    m.close()


def mostrar_archivo(k):
    taman = os.path.getsize(k)
    m = open(k, "rb")
    while m.tell() < taman:
        vec = pickle.load(m)
        print(vec)
    m.close()


def princiapl():
    op = -1
    vector = []
    cont = 0
    n = 0
    k = ""
    while op != 6:
        op = menu()
        if op == 1:
            n = int(input("Ingrese la cantidad de operaciónes agrícolas realizadas: "))
            n = validar_mayor_que(0, n)
            cont = cargar_arreglo(vector, n, cont)
        elif len(vector) > 0:
            if op == 2:
                mostrar(vector)
            elif op == 3:
                hacer_matriz(vector)
            elif op == 4:
                k = input("Ingrese el nombre de archivo deseado: ")
                prom = promedio(cont, n)
                crear_archivo(k, vector, prom)
            elif op == 5:
                if os.path.exists(k):
                    mostrar_archivo(k)
                else:
                    print("Primero realize el punto 4, genere el archivo antes de mostrarlo")


if __name__ == '__main__':
    princiapl()
