# Actividad N2
# Un binomio al cuadrado (suma) es igual al cuadrado del primer término,
# más el doble producto del primero por el segundo más el cuadrado del segundo.

# Plantear un script directamente en el shell de Python,
# que permita mostrar, para dos valores a y b, el valor del cuadrado del binomio.

print("El cuadrado de un binomio")
monomio1 = int(input("Ingrese el valor del primero monomio: "))
monomio2 = int(input("Ingrese el valor del segundo monomio monomio: "))

print("(", monomio1, "+", monomio2, ")²")
print(monomio1, "² + 2(", monomio1, "x", monomio2, ") +", monomio2, "²")

resultado = (monomio1 + monomio2)**2

print("El resultado es: ", resultado)
