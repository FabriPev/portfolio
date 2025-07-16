# 1 - Determinar la cantidad de palabras que tienen dos o más vocales pero no contienen una "s" (minúscula o mayúscula).
# Por ejemplo, en el texto “Los estudiantes rinden el parcial.” hay 2 palabras que cumplen con la condición ("rinden" y "parcial").

# 2 - Determinar el porcentaje de palabras (con respecto al total de palabras de texto) que finalizan en una consonante.
# Por ejemplo, en el texto: "El cielo es celeste." hay 4 palabras en total, y sólo 2 ("El" y "es") tienen una consonante
# como última letra. Por lo tanto, el porcentaje pedido es del 50%.

# 3 - Determinar cuántas palabras contienen (pero sin empezar con él) al último caracter de la primera palabra del texto
# (en minúscula o en mayúscula). Por ejemplo, en el texto: "Bienvenidos son los alumnos." la primera palabra finaliza
# con 's' y hay entonces 2 palabras que contienen a esa letra sin comenzar con ella ("los" y "alumnos").
# La palabra "son" contiene una "s", pero comienza con ella, y por lo tanto no debe ser contada.

# 4 - Determinar la cantidad de palabras que contienen la expresión "mi"
# (con cualquiera de sus letras en minúscula o en mayúscula) pero de forma que la palabra COMIENCE con esa expresión.
# Por ejemplo en el texto: “Mis amigos son miles.“, las palabras "Mis" y "miles" cumplen con la condición.
# Notar que "amigos" contiene "mi" pero no al inicio y por lo tanto no debe ser contada.

def es_vocal(carac):
    return carac in 'aeiouáéíóú'


def prom(contador_parical, contador_total):
    if contador_total > 0:
        promedio = (contador_parical * 100) / contador_total
        return promedio
    else:
        promedio = 0
        return promedio


def principal():
    texto = input('Ingrese texto: ')
    texto = texto.lower()

    cont_letras = cont_palabras = 0
    cant_vocales = 0
    cont_pal_fin_s = 0
    hay_s = False
    palabra_voc_s = 0
    letra = ult_car = None
    hay_ult_car_no_1 = False
    cont_pal_3 = 0
    hay_m = False
    hay_mi = False
    palabra_mi = 0

    for car in texto:
        if car != ' ' and car != '.':
            cont_letras += 1
            letra = car
            if es_vocal(car):
                cant_vocales += 1
            if car == "s":
                hay_s = True
            if ult_car == car and cont_letras != 1:
                hay_ult_car_no_1 = True
            if cont_letras == 1:
                if car == "m":
                    hay_m = True
            elif hay_m:
                if car == "i":
                    hay_mi = True
                else:
                    hay_m = False

        else:
            if cont_palabras == 0:
                ult_car = letra
            cont_palabras += 1
            if not es_vocal(letra):
                cont_pal_fin_s += 1
            if cant_vocales >= 2 and not hay_s:
                palabra_voc_s += 1
            if hay_ult_car_no_1:
                cont_pal_3 += 1
            if hay_mi:
                palabra_mi += 1
            hay_s = False
            cant_vocales = 0
            cont_letras = 0
            hay_ult_car_no_1 = False
            hay_m = hay_mi = False

    print(palabra_voc_s)
    print(round(prom(cont_pal_fin_s, cont_palabras), 2))
    print(cont_pal_3)
    print(palabra_mi)


if __name__ == '__main__':
    principal()
