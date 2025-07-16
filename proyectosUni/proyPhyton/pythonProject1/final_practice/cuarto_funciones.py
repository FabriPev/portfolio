class Cobro:
    def __init__(self, iden, puesto, monto, patente, hora):
        self.iden = iden
        self.puesto = puesto
        self.monto = monto
        self.patente = patente
        self. hora = hora

    def __str__(self):
        show = "Numero de identificacion: " + str(self.iden)
        show += " Puesto de cobro: " + str(self.puesto)
        show += " Monto cobrado: " + str(round(self.monto, 2))
        show += " Patente: " + str(self.patente)
        show += " Hora: " + str(self.hora) + "hs"
        return show


def validar_mayor_que(numero, minimo):
    while numero <= minimo:
        print("Numero no valido, Ingrese un numero mayor que: ", minimo)
        numero = int(input("Ingrese su nuevo numero"))
    return numero

def validar_entre(numero, minimo, maximo):
    while maximo > numero or numero < minimo:
        print("Numero no valido, ingrese un numero entre, ", minimo, "Y", maximo)
        numero = int(input("Ingrese su nuevo numero"))

    return numero
