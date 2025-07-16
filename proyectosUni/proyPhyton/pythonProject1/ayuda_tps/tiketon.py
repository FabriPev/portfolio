class Ticket:
    def _init_(self, codigo, patente, tipo, pago, pais, km):
        self.codigo = codigo
        self.patente = patente
        self.tipo = tipo
        self.pago = pago
        self.pais = pais
        self.km = km

    def _str_(self):
        r = " "
        r += "Código identificador del ticket: " + str(self.codigo)
        r += " - Patente del vehículo: " + str(self.patente)
        r += " - Tipo de vehículo: " + str(self.patente)
        r += " - Forma de pago: " + str(self.pago)
        r += " - País de la cabina: " + str(self.pais)
        r += " - Km recorridos desde la cabina anterior: " + str(self.km)

        return r