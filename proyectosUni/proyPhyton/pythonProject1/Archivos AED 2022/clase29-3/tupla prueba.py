import random
random.seed(31)

mult3 = mult5 = mult9 = 0
cant3 = cant5 = 0
mayimp = 0

for i in range(15000):
    num = random.randint(1, 55000)
    if num % 3 == 0 and num > 5000:
        mult3 += 1
        cant3 += num
    if num % 5 == 0 and num > 5000:
        mult5 += 1
        cant5 += num
    if num % 9 == 0 and num > 5000:
        mult9 += 1
    if num % 2 == 1:
        if mayimp < num:
            mayimp = num

prom3 = cant3 // mult3
prom5 = mult5 * 100 // 15000

print("-" * 189)
print("Cantidad de mayores a 5000 y divisibles por 3: ", mult3, "\n Cantidad de mayores a 5000 y divisibles por 5: ", mult5)
print("Cantidad de mayores a 5000 y divisibles por 9: ", mult9)
print("Promedio de mayores a 5000 y divisibles por 3: ", prom3)
print("El mayor de los numeros impares es : ", mayimp)
print("Promedio de mayores a 5000 y divisibles por 5: ", prom5)
print("-" * 189)
