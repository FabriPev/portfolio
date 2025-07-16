class Profesiones:
    def __init__(self, dni, nombre, importe, tipo_afil, tipo_trabaj):
        self.dni = dni
        self.nombre = nombre
        self.importe = importe
        self.tipo_afil = tipo_afil
        self.tipo_trabajo = tipo_trabaj

    def __str__(self):
        muestra = "Dni: " + str(self.dni)
        muestra += " Nombre: " + self.nombre
        muestra += " Importe: " + str(self.importe)
        muestra += " Tipo de afiliado: " + str(self.tipo_afil)
        muestra += " Tipo de trabajo: " + str(self.tipo_trabajo)

        return muestra




