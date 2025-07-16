import io

from tp4_clases import *
import os.path


def menu():
    cadena = 'Menu de Opciones:\n' \
             '1 --- Cargar vector\n' \
             '2 --- Filtrar por tag\n' \
             '3 --- Lenguajes\n' \
             '4 --- Popularidad\n' \
             '5 --- Buscar proyecto actualizado\n' \
             '6 --- Guardar populares\n' \
             '7 --- Mostrar archivo\n' \
             '8 --- Salir\n' \
             'Ingrese una opcion: '
    return int(input(cadena))


def add_in_order(vector, proyecto):
    n = len(vector)
    izq, der = 0, n - 1
    pos = n
    while izq <= der:
        c = (izq + der) // 2
        if vector[c].repositorio == proyecto.repositorio:
            pos = c
            break
        if vector[c].repositorio > proyecto.repositorio:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    vector[pos:pos] = [proyecto]


def str_to_proyecto(linea, reg_carg, vector, omit):
    token = linea.split("|")
    proyecto = []
    if token[4] != "":
        nombre_usuario = token[0]
        repositorio = token[1]
        descripcion = token[2]
        fecha_actu = token[3]
        lenguaje = token[4]
        likes = token[5]
        tags = token[6]
        url = token[7]
        if url == "":
            url = tags
            tags = ""
        proyecto = Proyecto(nombre_usuario, repositorio, descripcion, fecha_actu, lenguaje, likes, tags, url)
        add_in_order(vector, proyecto)
        reg_carg += 1
        return proyecto, reg_carg, omit
    else:
        omit += 1
        return proyecto, reg_carg, omit


def generar_arreglo(acu, vector, omit):
    if os.path.exists("proyectos.csv"):
        m = open("proyectos.csv", mode="rt")
        m.seek(1, io.SEEK_SET)
        for linea in m:
            proyecto, acu, omit = str_to_proyecto(linea, acu, vector, omit)
            vector.append(proyecto)
        m.close()
    return acu, vector, omit


def principal():
    vector = []
    opcion = -1
    reg_carg = 0
    reg_omit = 0
    while opcion != 8:
        opcion = menu()
        if opcion == 1:
            reg_carg, vector, reg_omit = generar_arreglo(reg_carg, vector, reg_omit)
            print(encabezado())
            print(to_string(vector))

        elif len(vector) > 0:
            if opcion == 2:
                pass

            elif opcion == 3:
                pass

            elif opcion == 4:
                pass

            elif opcion == 5:
                pass

            elif opcion == 6:
                pass

            elif opcion == 7:
                pass

            elif opcion == 8:
                print('Adios.')

            else:
                print('Usted debe ingresar una opcion correcta.')

        else:
            print('Primero debe cargar los datos en la opcion 1.')


if __name__ == '__main__':
    principal()

 #if vector[i].importe < n:
                #print(vector[i].nombre, "tiene el importe desactualizado")
            #else:
              #  print("Su importe no necesita actualizacion")
           # return
