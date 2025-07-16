def prom(numero_grande, numero_chico):
    promedio = numero_grande / numero_chico
    return promedio


def hay_dig(letra):
    if "0" <= letra <= "9":
        return True
    else:
        return False


def principal():
    texto = input('Ingrese un texto(finaliza con punto): ')
    texto = texto.lower()

    # inicializacion de variables
    cont_letras = cont_palabras = 0
    cont_digitos = 0
    ess_digito = False
    pal_digito = 0

    for car in texto:
        if car != '' and car != '.':
            cont_letras += 1
            if hay_dig(car) == True:
                ess_digito = True
                cont_digitos += 1
                print(cont_digitos)
            else:
                ess_digito = False


        else:
            if ess_digito == True:
                pal_digito += 1

            if cont_letras == 0:
                continue

            cont_palabras += 1

            # Reinicializar variables
            cont_letras = 0

        if car == ".":
            print(cont_digitos)
            media = prom(cont_digitos, pal_digito)
            print(media)


principal()
