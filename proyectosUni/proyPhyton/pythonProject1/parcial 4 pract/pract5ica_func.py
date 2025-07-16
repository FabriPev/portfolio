class Caso:
    def __init__(self, iden, descrip, monto, tipo, tribunal):
        self.iden = iden
        self.descrip = descrip
        self.monto = monto
        self.tipo = tipo
        self.tribunal = tribunal

    def __str__(self):
        show = "Numero de identificacion: " + str(self.iden)
        show += "| Descripcion del caso: " + self.descrip
        show += "| Monto asociado: " + str(self.monto)
        show += "| Codigo de tipo de caso: " + str(self.tipo)
        show += "| Tribuanl: " + str(self.tribunal)
        return show


def add_in_order(vector, caso):
    izq, der = 0, len(vector) - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if vector[c].iden == caso.iden:
            pos = c
        if vector[c].iden > caso.iden:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq

    vector[pos:pos] = [caso]


def validar_mayor_que(n, minimo):
    while n <= minimo:
        print("Numero no valido, ingrese un numero mayor a : ", minimo)
        n = int(input("Ingrese su nuevo numero: "))
    return n


def validar_entre(t, minimo, maximo):
    while minimo > t > maximo:
        print("Numero no valido, ingrese un numero entre", minimo, "y", maximo)
        t = int(input("Ingrese su nuevo numero: "))
    return t
