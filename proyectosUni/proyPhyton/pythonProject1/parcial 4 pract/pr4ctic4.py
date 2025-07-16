from pr4ctica_func import *
import random
import pickle
import os.path


def menu():
    op = "Menu de opciones\n" \
         "1----Cargar vector\n" \
         "2----Mostar vector\n" \
         "3----Generar matriz\n" \
         "4----Generar archivo\n" \
         "5----Mostar archivo\n" \
         "6----Salir\n" \
         "Ingrese su opcion: "
    return int(input(op))


def validar_mayor_Que(param, n):
    while n <= param:
        print("Numero no valido, ingrese un numero mayor que: ", param)
        n = int(input("Ingrese su nuevo numero"))
    return n


def generar_vector(vector, n):
    nom = ("Halo", "World of Warcraft", "Destiny II", "Dark souls II", "Dark souls 3", "God of war: Ragnarok", "Sims 4",
           "Overwatch 2", "Minecraft", "Age of empires II", "Fifa 23")
    for i in range(n):
        iden = random.randint(1, 900)
        nomb = random.choice(nom)
        stock = random.randint(0, 200)
        precio = random.randint(5000, 12000)
        origen = random.randint(0, 29)
        tipo = random.randint(0, 14)
        juegos = Juego(iden, nomb, stock, precio, origen, tipo)
        add_in_order(vector, juegos)


def mostar_vector(vector, p):
    for i in range(len(vector)):
        print(vector[i])


def validar_entre(p, minimo, maximo):
    while p > maximo or p < minimo:
        print("Numero no valido, ingrese un numero mayor que: ", minimo, "y menor que: ", maximo)
        p = "Ingrese un nuevo numero"
    return p


def generar_matriz(vector, x):
    mat = [[0] * 15 for i in range(30)]
    n = len(vector)
    for i in range(n):
        f = vector[i].origen
        c = vector[i].tipo
        mat[f][c] += 1

    for f in range(30):
        for c in range(15):
            if 0 < mat[f][c] <= x:
                print("En el pais", f, "hay una cantidad de ", mat[f][c], "juegos del tipo", c)


def generar_archivo(vector, k, cont_par, cont_tot):
    m = open(k, "wb")
    n = len(vector)
    for i in range(n):
        if vector[i].stock != 0:
            if vector[i].origen != 0 and vector[i].origen != 1:
                cont_tot += vector[i].precio
                cont_par += 1
                pickle.dump(vector[i], m)
    m.close()
    return cont_tot,


def mostrar_archivo(k, prom):
    m = open(k, "rb")
    taman = os.path.getsize(k)
    while m.tell() < taman:
        vec = pickle.load(m)
        print(vec)
    m.close()
    print("El promedio del precio de todos los juegos mostrados es: $", prom)

def principal():
    op = -1
    vector = []
    cont_tot = cont_par = 0
    k = ""
    while op != 6:
        op = menu()
        if op == 1:
            n = int(input("Ingrese la cantidad de juegos: "))
            n = validar_mayor_Que(0, n)
            generar_vector(vector, n)
        elif len(vector) > 0:
            if op == 2:
                p = int(input("Ingrese el codigo del pais de origen: "))
                p = validar_entre(p, 0, 29)
                mostar_vector(vector, p)
            elif op == 3:
                x = int(input("Ingrese el maximo para que el contador se muestre: "))
                generar_matriz(vector, x)
            elif op == 4:
                k = input("Ingrese el nombre de archivo deseado: ")
                generar_archivo(vector, k, cont_par, cont_tot)
            elif op == 5:
                if os.path.exists(k):
                    prome = prom(cont_tot, cont_par)
                    mostrar_archivo(k, prome)
                else:
                    print("Primero genere el archivo en el punto 4")


if __name__ == '__main__':
    principal()
