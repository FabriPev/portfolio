from tiketon import *
import os.path
import pickle


def crear_archivobinario(csv, binario):
    if os.path.exists(csv):
        print("Creando el archivo de registros...")
        mcsv = open(csv, "rt")

        linea = mcsv.readline()
        linea = mcsv.readline()

        mbin = open(binario, "wb")
        while True:
            linea = mcsv.readline()

            if linea == "":
                break

            separador = linea.split(",")
            codigo = int(separador[0])
            patente = separador[1]
            tipo = int(separador[2])
            pago = int(separador[3])
            pais = int(separador[4])
            km = int(separador[5])
            ticket = Ticket(codigo, patente, tipo, pago, pais, km)
            pickle.dump(ticket, mbin)

        mcsv.close()
        mbin.close()
        print("Listo...")
        respuesta = input("¿Desea eliminar el antiguo archivo? (s/n): ")
        if respuesta.lower() == 's':
            os.remove(csv)
            print("Archivo antiguo eliminado.")
        else:
            print("Operación cancelada. El archivo antiguo no ha sido eliminado.")
    else:
        print("El archivo", csv, "no existe...")
    print()


def validar_n(n):
    while n <= 0:
        print("Número no válido, ingrese un número mayor a cero.")
        n = int(input("Ingrese su nuevo número: "))
    else:
        return n


def val_patente(patente):
    posibles = "qwertyuiopasdfghjklñzxcvbnmQWERTYUIOPASDFGHJKLÑZXCVBNM1234567890"
    while not all(caracter in posibles for caracter in patente):
        print("Patente no valida")
        patente = input("Ingrese una nueva patente: ")
    else:
        return patente


def val_cod(codigo):
    while codigo < 1:
        print("Código identificador  no válido.")
        codigo = int(input("Ingrese un nuevo número de identificador: "))
    else:
        return codigo


def val_vehiculo(tipo):
    while 0 > tipo or tipo > 2:
        print("Tipo de vehículo no válido.")
        tipo = int(input("Ingrese un nuevo tipo de vehículo: "))
    else:
        return tipo


def val_pago(pago):
    while 1 > pago or pago > 2:
        print("Tipo de pago no es válido.")
        pago = int(input("Ingrese un nuevo tipo de pago: "))
    else:
        return pago


def val_cabina(pais):
    while 0 > pais or pais > 4:
        print("El número de cabina no es válido.")
        pais = int(input("Ingrese un nuevo número de cabina: "))
    else:
        return pais


def val_km(km):
    while 0 > len(str(km)) or len(str(km)) > 3:
        print("La cantidad de km no es válida.")
        km = int(input("Ingrese una nueva cantidad de km: "))
    else:
        return km


def crear_vector(v, n):
    for i in range(n):
        codigo = int(input("Ingrese el codigo identicador del ticket: "))
        codigo = val_cod(codigo)
        patente = input("Ingrese la patente del vehículo: ")
        patente = val_patente(patente)
        tipo = int(input("Ingrese el tipo de vehículo: "))
        tipo = val_vehiculo(tipo)
        pago = int(input("Ingrese la forma de pago: "))
        pago = val_pago(pago)
        pais = int(input("Ingrese el país donde está la cabina que hizo el cobro: "))
        pais = val_cabina(pais)
        km = int(input("Ingrese la distancia en kilómetros desde la última cabina de peaje que atravesó el vehículo: "))
        km = val_km(km)

        ticket = Ticket(codigo, patente, tipo, pago, pais, km)
        v.append(ticket)
    print("El vector ha sido creado correctamente")


def crear_archivob(v):
    m = open("tickets.dat", "ab")
    for i in range(len(v)):
        pickle.dump(v[i], m)
    m.close()


def mostrar_archivo(binario):
    if os.path.exists(binario):
        mbin = open(binario, "rb")
        t = os.path.getsize(binario)
        print("Listado de tickets...")
        while mbin.tell() < t:
            r = pickle.load(mbin)
            print(r)
        mbin.close()
        print("Listo...")
    else:
        print("El archivo", binario, "no existe...")
    print()


def mostrar_archivo_p(binario, v, p):
    cont = 0
    l = os.path.getsize(binario)
    if os.path.exists(binario):
        mbin = open(binario, "rb")
        t = os.path.getsize(binario)
        print("Listado de tickets...")
        while mbin.tell() < t:
            for i in range(l):
                r = pickle.load(mbin)
                if r[i].patente == p:
                    cont += 1
                    print(r[i])
                    print("Se resgistraron", cont, "patentes")
                else:
                    print("No se enccontró lo pedido")
            mbin.close()
            print("Listo...")
    else:
        print("El archivo", binario, "no existe...")


def principal():
    csv = "peajes-tp4.csv"
    binario = "tickets.dat"
    v = []
    opc = 0
    while opc != 9:
        print("Menú de opciones")
        print("1. Creación del archivo binario")
        print("2. Agregar datos al archivo binario")
        print("3. Mostrar el archivo binario archivo binario")
        print("4. Mostrar la patente que sea igual a p y el total")
        print("5. Mostrar el código de ticket que sea igual a c")
        print("6. Mostrar la cantidad total de combinaciones de vehículos")
        print("7. Cantidad total de vehículos contados por cada tipo de vehículo posible y ppr cada país de cabina "
              "posible")
        print("8. Distancia promedio")
        print("9. Salir")

        opc = int(input("Ingrese la opción que desee: "))

        if opc == 1:
            crear_archivobinario(csv, binario)
        elif opc == 2:
            n = int(input("Ingrese la cantidad de arreglos a cargar: "))
            v = [0] * n
            n = validar_n(n)
            crear_vector(v, n)
            crear_archivob(v)
        elif opc == 3:
            mostrar_archivo(binario)  # falta lo del país
        elif opc == 4:
            p = input("Ingrese la patente que desee buscar: ")
            mostrar_archivo_p(binario, v, p)  # error
        elif opc == 5:
            pass
        elif opc == 6:
            pass
        elif opc == 7:
            pass
        elif opc == 8:
            pass
        elif opc == 9:
            print("Ha finalizado")


if __name__ == '__main__':
    principal()