# 1 - Determinar la cantidad de palabras que contienen la lera "m" o la letra "o" (minúscula o mayúscula) a partir de la segunda letra
# (inclusive) de la palabra. Por ejemplo, en el texto “El Villareal de España juega en un estadio
# llamado el Madrigal.” hay 2 palabras cumplen con la condición (“llamado”, “estadio”)

# 2- Determinar el porcentaje de palabras (con respecto al total de palabras de texto) que contienen al menos 2 digitos.
# Por ejemplo, en el texto "Los cursos 1K14 y 1K15 rinden en turnos separados." hay 9 palabras y 2 de ellas cumplen el criterio
# ("1K14" y "1K15"), por lo tanto el porcentaje es 22.22%

# 3- Determinar la cantidad de palabras que contienen una vocal (minúscula o mayúscula) en todas las posiciones impares de dicha palabra.
# Por ejemplo, en el texto "La imagen incluye una claridad de luces." hay 2 palabras cumplen el criterio ("imagen" y "una").

# 4 - Determinar la cantidad de palabras que la expresión "pr" (con cualquiera de sus letras en minúscula o en mayúscula) pero de
# forma tal que la secuencia esté presente a partir del tercer caracter (incluido) de la palabra. Por ejemplo, en el texto
# La impronta del problema comprueba su dificultad." hay 2 palabras que cumplen el criterio ("impronta" y "comprueba").

def porc(contador_parcial, contador_total):
    if contador_total > 0:
        porcentaje = (contador_parcial * 100) / contador_total
        return porcentaje


def es_digito(letra):
    return letra in '0123456789'


def es_vocal(letra):
    return letra in 'aeiouáéíóú'


def principal():
    texto = input('Ingrese texto: ')
    texto = texto.lower()

    cont_letras = cont_palabras = 0
    hubo_m_o = hay_vocal = False
    cont_palabrasp1 = cont_digitos = 0
    cont_pal_digitos = palabra_vocal = 0
    hubo_p = False
    hubo_pr = False
    pr_palabra = 0

    for car in texto:
        if car != ' ' and car != '.':
            cont_letras += 1
            if cont_letras > 1:
                if car in 'moó':
                    hubo_m_o = True
            if es_digito(car):
                cont_digitos += 1
            if cont_letras == 1:
                hay_vocal = es_vocal(car)
            if cont_letras % 2 != 0 and hay_vocal:
                hay_vocal = es_vocal(car)
            if cont_letras >= 3:
                if car == 'p':
                    hubo_p = True
                elif hubo_p:
                    if car == "r":
                        hubo_pr = True
                    else:
                        hubo_p = False

        else:
            cont_palabras += 1
            if hubo_pr:
                pr_palabra += 1
            if hay_vocal:
                palabra_vocal += 1
            if hubo_m_o:
                cont_palabrasp1 += 1
                hubo_m_o = False

            if cont_digitos > 2:
                cont_pal_digitos += 1

            hay_vocal = False
            hubo_p = hubo_pr = False
            cont_letras = cont_digitos = 0

    porc_digit = porc(cont_pal_digitos, cont_palabras)

    print(round(porc_digit, 2), "%")
    print(palabra_vocal)
    print(pr_palabra)


if __name__ == '__main__':
    principal()
