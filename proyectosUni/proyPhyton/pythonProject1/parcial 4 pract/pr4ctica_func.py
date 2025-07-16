class Juego:
    def __init__(self, iden, nombre, stock, precio, origen, tipo):
        self.iden = iden
        self.nombre = nombre
        self.stock = stock
        self.precio = precio
        self.origen = origen
        self.tipo = tipo

    def __str__(self):
        show = "Numero de identificacion: " + str(self.iden)
        show += "| Nombre: " + self.nombre
        show += "| Stock disponible: " + str(self.stock)
        show += "| Precio: " + str(self.precio)
        show += "| Codigo del pais de origen: " + str(self.origen)
        show += "| Codigo del tipo de juego: " + str(self.tipo)

        return show


def add_in_order(vector, juego):
    izq, der = 0, len(vector) - 1
    pos = 0
    while izq <= der:
        c = (izq + der) // 2
        if vector[c].nombre == juego.nombre:
            pos = c
            break
        if vector[c].nombre > juego.nombre:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq

    vector[pos:pos] = [juego]

def prom(total, par):

    if par == 0:
        print("No se puede realizar el promedio")
    else:
        prome = total / par
        prome = round(prome, 2)
        return prome
