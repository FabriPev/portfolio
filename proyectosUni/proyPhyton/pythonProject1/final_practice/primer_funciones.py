class Departamento:
    def __init__(self, identifi, inquilino, piso, estado, monto):
        self.identificacion = identifi
        self.inquilino = inquilino
        self.piso = piso
        self.estado = estado
        self.monto = monto

    def __str__(self):
        show = "Numero del Departamento: " + str(self.identificacion)
        show += "| Nombre del inquilino: " + self.inquilino
        show += "| Piso Nº: " + str(self.piso)
        show += "| Estado del departamento: " + str(self.estado)
        show += "| Manto a pagar de gastos comunes: " + str(round(self.monto, 2))

        return show


def to_string_campos():
    cad = '{:<10}'.format('Numero')
    cad += '{:<40}'.format('Inquilino')
    cad += '{:<6}'.format('Piso')
    cad += '{:<7}'.format('Estado')
    cad += '{:<10}'.format('Expensas')
    return cad


def to_string(departamento):
    cad = '{:<10}'.format(departamento.identificacion)
    cad += '{:<40}'.format(departamento.inquilino)
    cad += '{:<6}'.format(departamento.piso)
    cad += '{:<7}'.format(departamento.estado)
    cad += '${:<10.2f}'.format(departamento.monto)
    return cad

