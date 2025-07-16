# Actividad N1
# Plantear un script (directamente en el shell de Python) que permita informar,
# para dos valores a y b el resultado de la división a/b y el resto de esa divisón.

print("Cálculo de division")
dividendo = int(input("Ingrse un número a dividir:"))
divisor = int(input("Ingrese en cuantas partes quiere dividir el número anterior"))

print(dividendo, "/", divisor)

cociente = dividendo/divisor

print("El resultado de la división es:", cociente)
