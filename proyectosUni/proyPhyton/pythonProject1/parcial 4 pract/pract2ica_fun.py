class Empleos:

    def __init__(self, iden, descrip, monto, ciudad, tipo):
        self.iden = iden
        self.descrip = descrip
        self.monto = monto
        self.ciudad = ciudad
        self.tipo = tipo

    def __str__(self):
        show = "Numero de indentifiacion: " + str(self.iden)
        show += "| Descripcion del empleo: " + self.descrip
        show += "| Monto a pagar: " + str(self.monto)
        show += "| Ciudad: " + str(self.ciudad)
        show += "| Tipo de empleo: " + str(self.tipo)
        return show


def write(k):
    print("Numero de indentifiacion: ", str(k.iden), end="|")
    print("Descripcion del empleo: ", k.descrip, end="|")
    print("Monto a pagar: ", str(k.monto), end="|")
    print("Ciudad: ", str(k.ciudad), end="|")
    print("Tipo de empleo: ", str(k.tipo))

