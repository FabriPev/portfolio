class Trabajo:
    def __init__(self, numid, trabaj, tip, imp, cant):
        self.numero = numid
        self.nombre = trabaj
        self.tipo = tip
        self.importe = imp
        self.cantidad = cant

    def __str__(self):
        tipos = ("tipo1", "tipo2", " tipo3")
        r = 'Tipo: ' + tipos[self.tipo]
        return r
