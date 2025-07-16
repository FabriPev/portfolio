# Actividad N7
# Se desea conocer el precio de un boleto de viaje en ómnibus de media distancia.
# Para el cálculo del mismo se debe considerar el monto base (que se cobra siempre),
# más un valor extra calculado en base a la cantidad de kilómetros a recorrer:  Por cada kilómetro a recorrer se cobra $0.30 de adicional.

print("Calcula el precio de tu boleto")

mb = float(input("Ingrese el monto base: "))
km = float(input("¿Cuál es la distancia hasta su lugar objetivo? (indiquelo en km): "))

preciot = mb+(km*0.30)

print("El precio de su boleto es:", preciot)
