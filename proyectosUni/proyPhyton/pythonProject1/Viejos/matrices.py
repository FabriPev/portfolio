import random


def cargar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = random.randint(1, 20)


def mostrar_matriz_fc(matriz):
    for i in range(len(matriz)):  # recorro filas
        for j in range(len(matriz[i])):  # recorro columnas
            print("Fila", i, "- Col", j, ":", matriz[i][j])


def mostrar_matriz_cf(matriz):
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            print("Fila", i, "- Col", j, ":", matriz[i][j])


def totalizar_fila(matriz):
    acu = 0
    for i in range(len(matriz)):
        acu += matriz[i][0]
    print("Total de fila 0:", acu)


def totalizar_columnas(matriz):
    cols = len(matriz[0])
    acu_col = [0] * cols
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            acu_col[j] += matriz[i][j]
    print("Total por fila:", acu_col)


def totalizar_filas(matriz):
    f = len(matriz)
    acu_fil = [0] * f
    for i in range(f):
        for j in range(len(matriz[i])):
            acu_fil[i] += matriz[i][j]
    print("Total por fila:", acu_fil)


def principal():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    # print(m)
    # print(m[2][1])

    m1 = [0] * 4  # creamos las filas
    for i in range(len(m1)):  # recorremos cada fila
        m1[i] = [0] * 3  # creamos las columnas
       # print (m1)

    mat = [[0] * 3 for f in range(4)]
    print(mat)
    print("Matriz m")
    mostrar_matriz_fc(m)
    print("Matriz m1")
    mostrar_matriz_fc(m1)
    print("Matriz mat")
    mostrar_matriz_fc(mat)
    cargar_matriz(m1)
    print("Matriz m1 con datos")
    mostrar_matriz_fc(m1)
    cargar_matriz(mat)
    print("Matriz mat con datos")
    mostrar_matriz_fc(mat)
    print("Matriz m columnas y filas")
    mostrar_matriz_cf(m)
    totalizar_fila(m)
    totalizar_columnas(m)
    totalizar_filas(m)


if __name__ == '__main__':
    principal()
