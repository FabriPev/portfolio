class Gasto:
    def __init__(self, cod, desc, mes, suc, imp):
        self.codigo = cod
        self.descripcion = desc
        self.mes = mes
        self.sucursal = suc
        self.importe = imp

    def __str__(self):
        mensaje = "Código: " + str(self.codigo)
        mensaje += " - Descipción: " + self.descripcion
        mensaje += " - Mes: " + str(self.mes)
        mensaje += " - Sucursal: " + str(self.sucursal)
        mensaje += " - Importe: $" + str(self.importe)
        return mensaje


def write(gasto):
    print("Código:", gasto.codigo, end = "-")
    print("Descripción:", gasto.descripcion, end = "-")
    print("Mes:", gasto.mes, end = "-")
    print("Sucursal:", gasto.sucursal, end = "-")
    print("Importe: $", gasto.importe)


def to_string(gasto):
    mensaje = "Código: " + str(gasto.codigo)
    mensaje += " - Descripcion:" + gasto.descripcion
    mensaje += " - Mes: " + str(gasto.mes)
    mensaje += " - Sucursal: " + str(gasto.sucursal)
    mensaje += " - Importe: $" + str(gasto.importe)
    return mensaje


def test():
    reg = Gasto(1, "Agua", 2, 0, 3456.3)
    print(reg)


if __name__ == '__main__':
    test()

