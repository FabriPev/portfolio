import random
import pickle
import os.path
from funciones import *


def menu():
    op = "Menu de opciones\n" \
         "1----Cargar los datos\n" \
         "2----Mostar el arreglo\n" \
         "3----Buscar arreglo por dni\n" \
         "4----Crear archivo\n" \
         "5----Mostar archivo\n" \
         "6----Buscar arreglo por nombre\n" \
         "7----Determine la cantidad de profesionales de cada posible tipo d afiliación por cada posible tipo de " \
         "trabajo \n" \
         "8----Salir\n" \
         "Ingrese se opcion: "

    return int(input(op))


def validar_mayor_a(n, b):
    while n <= b:
        print("Numero no valido, ingrese un numero mayor a ", b)
        n = int(input("Ingrese su nuevo numero: "))

    return n


def add_in_order(vector, nuevo):
    izq, der = 0, len(vector) - 1
    pos = 0
    while izq <= der:
        med = (izq + der) // 2
        if vector[med].dni == nuevo.dni:
            pos = med
            break
        if nuevo.dni > vector[med].dni:
            izq = med + 1
        else:
            der = med - 1

    if der < izq:
        pos = izq

    vector[pos:pos] = [nuevo]


def cargar_vector(n, vector):
    names = ("Pedro", "Camila", "Jazmin", "Milagros", "Pilar", "Juan", "Lucas")
    sec_name = ("Perez", "Vegas", "Fernandez", "Gonzales", "Peveraro")
    for i in range(n):
        dni = str(random.randint(35, 40)) + str(random.randint(100, 999)) + str(random.randint(100, 999))
        nombre = random.choice(names) + " " + random.choice(sec_name)
        money = random.randint(2000, 10000)
        afil = random.randint(0, 4)
        trabaj = random.randint(0, 14)
        profesion = Profesiones(dni, nombre, money, afil, trabaj)
        add_in_order(vector, profesion)


def buscar_nombre(nom, vector, ):
    for i in range(len(vector)):
        if nom == int(vector[i].nombre):
            print(vector[i])
            break

    print("No hay un profesional con ese nombre ")


def mostar(v):
    for i in range(len(v)):
        print(v[i])


def cargar_archivo(k, vector, n):
    m = open(k, "wb")
    for i in range(len(vector)):
        if 3 <= vector[i].tipo_trabajo >= 5:
            if vector[i].importe > n:

                pickle.dump(vector[i], m)
    m.close()


def buscar_dni(doc, vector, p):
    izq, der = 0, len(vector)

    while izq <= der:
        c = (izq + der) // 2
        if doc == vector[c].dni:
            print(vector)
            if vector[c].importe < p:
                print(vector[c].importe, "tiene el importe desactualizado")
            elif vector[c].importe > p:
                print("Su importe no necesita actualizacion")

            break

        if doc < int(vector[c].dni):
            der = c - 1
        else:
            izq = c + 1

    print("No hay ningun profesional con ese dni")


def principal():
    vector = []
    op = -1
    k = ""
    punto_4 = False
    punto_1 = False
    while op != 8:
        op = menu()
        if op == 1:
            punto_1 = True
            n = int(input("Ingrese la cantidad de arreglos a cargar: "))
            n = validar_mayor_a(n, 0)
            cargar_vector(n, vector)
        if punto_1:
            if op == 2:
                mostar(vector)
            if op == 3:
                doc = int(input("Ingrese el dni a buscar: "))
                p = int(input("Ingrese el nuevo importe: "))
                p = validar_mayor_a(p, 0)
                buscar_dni(doc, vector, p)
            if op == 4:
                k = input("Ingrese el nombre de archivo deseado: ")
                monto = int(input("Importe minimo para grabar: "))
                monto = validar_mayor_a(monto, 0)
                cargar_archivo(k, vector, monto)
                punto_4 = True

            if punto_4:
                if op == 5:
                    m = open(k, "rb")
                    t = os.path.getsize(k)
                    while m.tell() < t:
                        pro = pickle.load(k)
                        mostar(pro)
            else:
                print("Primero cree en archivo")

            if op == 6:
                nom = input("Ingrese el nombre a buscar, separe nombre y apellido por un espacio")
                buscar_nombre(nom, vector)

        else:
            print("Primero realize el punto 1 ")


if __name__ == '__main__':
    principal()
