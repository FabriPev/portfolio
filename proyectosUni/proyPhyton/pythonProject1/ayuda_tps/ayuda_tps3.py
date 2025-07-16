from trabajin import *
import random


# def validar(inf):
#    n = inf
#    while n <= inf:
#       n = int(input('Valor (mayor a ' + str(inf) + '): '))
#       if n <= inf:
#           print('Error: se pidio mayor a', inf, '... cargue de nuevo...')
#    return n


# def validate_type(mn=0, mx=3):
#    cod = int(input('Ingrese tipo (>= ' + str(mn) + ' y <= ' + str(mx) + '): '))
#    while cod < mn or cod > mx:
#        cod = int(input('Error... era >='+str(mn)+' y <='+str(mx)+'). De nuevo: '))
#    return cod


def cant_por_tipo(v, vec_acu):
    vec_acu = [0]*4
    for i in range(len(v)):
        vec_acu[v[i].tipo] += 1




def bus_sec(v):
    mayor = None
    n = len(v)
    for i in range(n):
        if mayor == None:
            mayor = v[i]
        elif mayor < v[i].cantidad:
            mayor = v[i]
    print(mayor)

def carga(v):
    tb = ("torre", "casa", "hotel", "progamador", "tecnico",)
    print("cargue los datos:")
    for i in range(len(v)):
        print("cargue numero")
        numid = random.randint(1, 100)

        print("cargue trabajos:")
        trabaj = random.choice(tb)

        print("tipo:")
        tip = random.randint(0, 3)

        print("importe")
        imp = random.uniform(1, 100)

        print("personal:")
        cant = random.randint(1, 50)

        v[i] = Trabajo(numid, trabaj, tip, imp, cant)


def mostrar(v):
    print("listado de trabajos")
    n = len(v)
    for i in range(n):
        print(v[i])


def ordenar(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].importe < v[j].importe:
                v[i], v[j] = v[j], v[i]


def main():
    v = []
    vec_acu = [0]
    opc = 0
    while opc != 6:
        print('\nMenu de opciones:')
        print('1. Cargar trabajos')
        print('2. Mostrar trabajos ordenados por número')
        print('3. Contar trabajos por tipo')
        print('4. Buscar trabajo')
        print('5. cant trabajos por tipo')

        opc = int(input("ingrese su eleccion:"))

        if opc == 1:
            n = int(input("ingrese cantidad de trabajos:"))
            v = [0] * n
            print("¿Cuántos trabajos va a cargar?:")
            carga(v)
            print("Carga completa...")



        elif opc == 2:
            if len(v) != []:
                mostrar(v)
                ordenar(v)
            else:
                print("No está cargado el vector...")

        elif opc == 3:
            pass



        elif opc == 4:
            pass


        elif opc == 5:
            print("programa finalizado")


if __name__ == '__main__':
    main()
