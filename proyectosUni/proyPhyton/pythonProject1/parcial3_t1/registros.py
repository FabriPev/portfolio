class Paseos:
    def __init__(self, iden_pas, nom_clien, apell_clien, tip_pas, monto):
        self.nomb = iden_pas
        self.nombre_clien = nom_clien
        self.apell_clien = apell_clien
        self.tipo = tip_pas
        self.monto = monto


def write(paseo):
    for i in range(len(paseo)):
        print("Identificacion de paseo: ", paseo[i].nomb, end="-")
        print("Nombre del cliente: ", paseo[i].nombre_clien, end="-")
        print(paseo[i].apell_clien, end="-")
        print("Tipo de paseo: ", paseo[i].tipo, end="-")
        print("Monto a abonar: ", paseo[i].monto)


def mayor_a(cota_inf, mensaje="Ingrese un numero: "):
    num = cota_inf
    while num <= cota_inf:
        num = int(input(mensaje))
        return num


def ordenar(vector):
    n = len(vector)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if vector[i].iden_pas < vector[j].iden_pas:
                vector[i], vector[j] = vector[j], vector[i]
