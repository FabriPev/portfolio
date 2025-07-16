class Servicio:
    def __init__(self, iden, descrip, importe, tipo, zona):
        self.iden = iden
        self.descrip = descrip
        self.importe = importe
        self.tipo = tipo
        self.zona = zona

    def __str__(self):
        show = "Numero de identificacion: " + str(self.iden)
        show += "| Descipcion: " + self.descrip
        show += "| Importe a facturar: " + str(self.importe)
        show += "| Tipo de operacion: " + str(self.tipo)
        show += "| Zona geografica: " + str(self.zona)

        return show


def promedio(total, cant):
    prom = total / cant
    round(prom, 2)
    return prom
