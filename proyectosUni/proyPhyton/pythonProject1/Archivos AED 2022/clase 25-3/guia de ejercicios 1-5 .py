# Clase de 25/03

# Actividad N5
# Desarrolle un programa para convertir una medida dada en pies a sus equivalentes en:
#
# yardas
# pulgadas
# centímetros
# metros

print("Conversor de unidades, pies a distintas unidades")
pies = int(input("Ingrese su número: "))

yardas = pies / 3

pulgadas = pies * 12

centimetros = pulgadas * 2.54

metros = centimetros / 100

print("En", pies, "pies hay:", pulgadas, "pulgadas")
print("En", pies, "pies hay:", yardas, "yardas")
print("En", pies, "pies hay:", centimetros, "centimetros")
print("En", pies, "pies hay:", metros, "metros")
