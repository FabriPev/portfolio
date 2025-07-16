class Factura:
    def __init__(self, numero, imp, tipfac, ap, tipper):
        self.numero = numero
        self.importe = imp
        self.tipo = tipfac
        self.apellido = ap
        self.tipo_perfum = tipper


def write(factura):
    print("Numero de Factura: ", factura.numero, )
    print("Importe de la factura: ", factura.importe)
    print("Tipo de factura: ", factura.tipo)
    print("Apellido del comprador: ", factura.apellido)
    print("tipo de perfume", factura.tipo_perfum)


def validacion_entre(numero, cota_inf, cota_mayor):
    while cota_inf > numero > cota_mayor:
        numero = int(input("Numero no valido, Ingrese un numero mayor a: ", cota_inf, " y menor a ", cota_mayor))
    return numero

def validacion_mayor_a(numero, cota_inf):
    if numero < cota_inf:
        print("numero no valido. Ingrese un nuevo numero")
