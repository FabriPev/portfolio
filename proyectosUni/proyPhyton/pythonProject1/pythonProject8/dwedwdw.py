import random
# Se pide desarrollar un programa controlado por menu de opciones que permita realizar las siguientes operaciones:
#
# a) Ingresar un secuencia de n números, validar que n sea mayor a cero, y determinar cual la cantidad de los números
# múltiplos de 3 y 5, y que porcentaje representan sobre el total de números
#
# b) Ingresar un texto, el mismo termina con punto, determinar cuantas palabras de mas de 4 letras hay en el texto
#
# c)  Ingresar el nombre y las notas finales de tres alumnos de postgrado, indicar el nombre del alumno con peor nota
# de los tres
#
# d) Salir

Menu = "Menu de opciones : \n" + \
                 "\t1) Determinar cantidad de multiplos 3 y 5 y representar porcentaje.\n" + \
                 "\t2) Determinar cuantas palabras de mas de 4 letras hay.\n" + \
                 "\t3) Indicar el nombre del alumno con la peor nota.\n" + \
                 "\t0) Salir.\n" + \
                 "\t Ingrese su opcion: "

opcion = -1
while opcion != 0:
    opcion = int(input(Menu))
    if opcion == 1:
        n = 0
        while n <= 0:
            n = int(input("Ingrese la cantidad de numeros que desea procesar: "))
            if n <= 0:
                print("¡¡Error!!, ingrese un numero mayor a 0")
        cont_mult35 = 0
        for i in range(n):
            num = random.randint(1, 1500)
            if num % 3 == 0 and num % 5 == 0:
                cont_mult35 += 1
        porcentaje = cont_mult35 * 100 / n
    elif opcion == 2 :
        texto = input("Ingrese un texto( debe terminar en .): ")
        cont_letras = cont_palabras =0
        for letras in texto:
            if letras != " " and letras != ". ":
                cont_letras += 1
            else:
                if cont_letras > 0:
                    if cont_letras > 4:
                        cont_palabras = +1
                cont_letras = 0
        print("Cantidad de palabras con mad de 4 letras : ", cont_palabras)
    elif opcion == 3:
        nomb1 = input("Ingrese el nombre del primer alumno: ")
        nota1 = int(input("Ingrese su nota: "))
        nomb2 = input("Ingrese el nombre del segundo alumno: ")
        nota2 = int(input("Ingrese su nota: "))
        nomb3 = input("Ingrese el nombre del tercer alumno: ")
        nota3 = int(input("Ingrese su nota: "))
        mal = nota1
        if nota2 < nota1:
            mal = nota2
        elif nota3 < mal:
            mal = nota3
        print("La peor nota es: ", mal)
    elif opcion == 0:
        print("Saliste")
        break

    else:
        print("Valor invalido")
