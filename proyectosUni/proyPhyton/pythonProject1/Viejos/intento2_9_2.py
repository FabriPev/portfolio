class Alumnos:
    def __init__(self, dnia, namea, apella, dnit, impor, nivel):
        self.dnia = dnia
        self.nombre_alum = namea
        self.apellido_a = apella
        self.dni_tut = dnit
        self.cuota = impor
        self.nivel = nivel


def write(alumno):
    print("Dni del alumno: ", alumno.dnia, end="-")
    print("Nombre completo del alumno: ", alumno.nombre_alum, end=" ")
    print(alumno.apellido_a, end="-")
    print("Dni del tutor a cargo: ", alumno.dni_tut, end="-")
    print("Importe a pagar: ", alumno.cuota, end="-")
    print("Nivel del alumno: ", alumno.nivel)


def mayor_a(cota_inf, mensaje="Ingrese un numero: "):
    numero = cota_inf
    while numero <= cota_inf:
        numero = int(input(mensaje))
        if numero <= cota_inf:
            print("El numero debe ser mayor a: ", cota_inf)
    return numero
