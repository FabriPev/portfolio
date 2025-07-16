from intento2_9_2 import *
import random


def menu():
    cadena = 'Menu de Opciones\n' \
             '============================================\n' \
             '1 ------ Cargar Arreglo de Alumnos\n' \
             '2 ------ Mostrar los datos de las Alumnos\n' \
             '3 ------ Mostrar Cantidad de alumnos por nivel\n' \
             '4 ------ Determinar Monto Total a Abonar por Tutor\n' \
             '5 ------ Buscar Alumno\n' \
             '0 ------ Salir\n' \
             'Ingrese su opcion: '
    return int(input(cadena))


def cargar_alumnos(cant):
    v = []
    nombres = "Pedro", "Camilia", "Valentina", "Santiago", "Lucia", "Tomas"
    apellidos = "Gutierrez", "Sanchez", "Lopez", "Martinez", "Zamboni"
    for i in range(cant):
        dnia = str(random.randint(40, 50)) + str(f"{random.randint(1, 999999):0>6}")
        namea = random.choice(nombres)
        apella = random.choice(apellidos)
        dnitut = str(random.randint(20, 35)) + str(f"{random.randint(1, 999999):0>6}")
        importe = round(random.uniform(4000, 10000), 2)
        nivel = random.randint(0, 12)
        alumno = Alumnos(dnia, namea, apella, dnitut, importe, nivel)
        v.append(alumno)

    return v


def ordenar(vector):
    for i in range(len(vector) - 1):
        for j in range(i + 1, len(vector)):
            if vector[i].nombre_alum > vector[j].nombre_alum:
                vector[i], vector[j] = vector[j], vector[i]


def acumlar(alumnos, contador):
    num = 0

def principal():
    opcion = -1
    vector_alumnos = []
    cont = []
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            cant = mayor_a(0, "Ingrese la cantidad de alumnos: ")
            vector_alumnos = cargar_alumnos(cant)
        if len(vector_alumnos) > 0:
            if opcion == 2:
                ordenar(vector_alumnos)
                write(vector_alumnos)
            elif opcion == 3:
                cont = [] * 13

            elif opcion == 4:
                pass
            elif opcion == 5:
                pass


if __name__ == '__main__':
    principal()
