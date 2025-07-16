from prueba_parcial import *
import random
__author__ = 'Algoritmos y Estructuras de Datos'



def menu():
    cadena = 'Menu de Opciones\n' \
             '============================================\n' \
             '1 ------ Cargar Arreglo de Ventas\n' \
             '2 ------ Mostrar los datos de las Ventas\n' \
             '3 ------ Mostrar Total Facturado por Perfume\n' \
             '4 ------ Mostrar Datos de Facturas por Rango\n' \
             '5 ------ Buscar Factura\n' \
             '0 ------ Salir\n' \
             'Ingrese su opcion: '
    return int(input(cadena))


def carga_auto(n):
    vector = [None] * n
    for pos in range(n):
        numero = 10
        imp = int(input("Ingrese el importe de la venta: "))
        imp = validacion_entre(imp, 0, 200000)

def principal():
    opcion = -1
    ventas = []
    while opcion != 0:
        opcion = menu()
        if opcion == 1:
            cant = int(input("Ingrese la cantidad de perfumes vendidos: "))

            while cant < 0:
                cant = int(input("Cantidad no valida. Ingrese su nueva cantidad: "))
            else:
                carga_auto(cant)

        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass



if __name__ == '__main__':
    principal()
