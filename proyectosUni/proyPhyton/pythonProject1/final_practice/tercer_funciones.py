class Ticket:
    def __init__(self, numero, nombre_peli, tipo_proyec, clasificacion, precio, dia):
        self.numero = numero
        self.nombre = nombre_peli
        self.tipo = tipo_proyec
        self.clasificacion = clasificacion
        self.precio = precio
        self.dia = dia

    def __str__(self):
        clasificacion = ("ATP", "M13", "M16", "M18")
        proyecciones = ("Normal", "3D", "IMAX", "IMAX 3D")
        self.clasificacion = clasificacion[self.clasificacion]
        self.tipo = proyecciones[self.tipo - 1]
        show = "Numero de ticket: " + str(self.numero)
        show += "|Nombre de película: " + self.nombre
        show += "|Tipo de proyección: " + self.tipo
        show += "|Clasificación: " + str(self.clasificacion)
        show += "|Precio de la entrada: " + str(self.precio)
        show += "|Dia de proyección: " + str(self.dia)
        return show


def validar_entre(n, minimo, maximo):
    while minimo > n or n > maximo:
        print("Numero no valido, ingrese un numero entre: ", minimo, " y ", maximo)
        n = int(input("Ingrese su nuevo numero: "))
    else:
        return n
