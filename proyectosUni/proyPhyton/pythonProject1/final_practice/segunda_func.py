class Mudanza:
    def __init__(self, identificacion, destino, codigo, tarifa, carga):
        self.identi = identificacion
        self.destino = destino
        self.codigo = codigo
        self.tarifa = tarifa
        self.carga = carga

    def __str__(self):
        show = "|Numero de identificacion: " + str(self.identi)
        show += "|Destino: " + str(self.destino)
        show += "|Codigo del vehiculo: " + str(self.codigo)
        show += "|Tarifa a pagar: " + str(round(self.tarifa, 2))
        show += "|Tipo de carga: " + str(self.carga)
        return show


def validar_mayor_que(n, minimo):
    while n <= minimo:
        print("¡¡Numero no valido! Ingrese un numero mayor que", minimo)
        n = int(input("Ingrese su nuevo numero: "))
    else:
        return n


def sacar_promedio(chico, grande):
    if chico == 0:
        return "No se puede sacar promedio"

    else:
        prom = grande // chico

        return prom
