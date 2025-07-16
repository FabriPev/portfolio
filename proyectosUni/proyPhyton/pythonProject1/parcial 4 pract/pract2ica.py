from pract2ica_fun import *
import random
import pickle
import os.path


def menu():
    op = "Menu de opcion \n" \
         "1----Cargar arreglo\n" \
         "2----Mostar arreglo\n" \
         "3----Determine la cantidad de empleos ofrecidos para cada posible ciudad y por cada posible tipo\n" \
         "4----Crear archivo\n" \
         "5----Mostar archivo\n" \
         "6----Salir\n" \
         "Ingrese su opcion: "

    return int(input(op))


def mayor_que(param, n):
    while param <= n:
        print("Nunmero no valido, ingrese un numero mayor a ", n)
        param = int(input("Ingrese su nuevo numero: "))
    return param


def valor_entre(n, cota_inf, cota_sup):
    while n > cota_sup or n < cota_inf:
        print("Numero valido ingrese un numero entre ", cota_inf, " y ", cota_sup)
        n = int(input("Ingrese su nuevo numero "))
    return n


def add_in_order(empleo, vector):
    izq, der = 0, len(vector) - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if empleo.iden == vector[c]:
            pos = c
            break
        if vector[c].iden > empleo.iden:
            der = c - 1
        else:
            izq = c + 1
    if der < izq:
        pos = izq
    vector[pos:pos] = [empleo]


def cargar_vector(n, vector):
    des = ("Recolector de basura", "Constructor", "Oficinista", "Vendedor", "Alto cargo")
    for i in range(n):
        iden = random.randint(0, 100)
        descrip = random.choice(des)
        monto = random.randint(50000, 150000)
        ciudad = random.randint(0, 29)
        tipo = random.randint(0, 19)
        empleo = Empleos(iden, descrip, monto, ciudad, tipo)
        add_in_order(empleo, vector)


def mostrar(vector):
    for i in range(len(vector)):
        print(vector[i])


def matriz(vector, a, b):
    mat = [[0] * 20 for f in range(30)]
    n = len(vector)
    for u in range(n):
        i = vector[u].ciudad
        j = vector[u].tipo
        mat[i][j] += 1

    for i in range(30):
        for j in range(20):
            if a <= mat[i][j] <= b:
                print(mat[i][j])
                print('Ciudad', i, 'Tipo', j, 'Cantidad de empleos:', mat[i][j])


def crear_archivo(k, vector, cont):
    plata = int(input("Ingrese el monto minimo a pagar para que el arreglo sea guardado: "))
    plata = mayor_que(plata, 0)
    m = open(k, "wb")
    n = len(vector)
    for i in range(n):
        if vector[i].monto > plata and vector[i].tipo <= 15:
            pickle.dump(vector[i], m)
            cont += 1
    m.close()
    return cont


def leer_archivo(k, cont):
    m = open(k, "rb")
    n = os.path.getsize(k)

    while m.tell() < n:
        r = pickle.load(m)
        print(r)

    m.close()


def principal():
    op = -1
    punto_1 = False
    vector = []

    cont = 0
    k = ""
    while op != 6:
        op = menu()
        if op == 1:
            punto_1 = True
            n = mayor_que(int(input("Cuantos arreglos dese hacer: ")), 0)
            cargar_vector(n, vector)
        elif punto_1:
            if op == 2:
                mostrar(vector)
            elif op == 3:
                a = mayor_que(int(input("Ingrese el minimo del contador para mostrar: ")), -1)
                b = mayor_que(int(input("Ingrese el maximo del contador para mostar: ")), a)
                matriz(vector, a, b)
            elif op == 4:
                k = input("Ingrese el nombre de archivio deseado para crearclo: ")
                cont = crear_archivo(k, vector, cont)

            elif op == 5:
                if not os.path.exists(k):
                    print("¡¡¡ERROR!!!")

                    print("Primero realize el punto 4")
                else:
                    leer_archivo(k, cont)


if __name__ == '__main__':
    principal()
