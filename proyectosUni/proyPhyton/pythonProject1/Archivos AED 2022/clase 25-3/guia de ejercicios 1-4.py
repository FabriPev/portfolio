# Actividad N4

# ¿Cómo usaría el operador resto (%) para obtener el valor del último dígito de un número entero?
# ¿Y cómo obtendría los dos últimos dígitos?
# Desarrolle un programa que cargue un número entero por teclado,
# y muestre el último dígito del mismo (por un lado) y los dos últimos dígitos (por otro lado)

print("Últimos dígitos de un número")

numerito = int(input("Deje su número: "))

digito1 = numerito % 10

digito2 = numerito % 100

print("El ultimo dígito de su numero es: ", digito1)

print("Los dos últimos dígitos de su numero son: ", digito2)
