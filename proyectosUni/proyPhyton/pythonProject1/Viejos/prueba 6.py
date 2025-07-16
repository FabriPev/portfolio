# 1 - Determinar la cantidad de palabras que tienen dos o más vocales (minúsculas o mayúsculas) y que no contienen ni "q"
# ni "z"  (minúsculas o mayúsculas). Por ejemplo, en el texto:
# "Los cursos se evalúan con quiz." hay 2 palabras que cumplen con la condición: "cursos" y "evalúan".

# 2 - Determinar la cantidad de palabras que tienen la segunda letra (minúscula o mayúscula) igual que su última letra
# (minúscula o mayúscula). Por ejemplo, en el texto: "Hola casa azul." hay 1 palabra ("casa") que cumple con la condición.

# 3 - Determinar cuántas palabras de longitud mayor a dos, empiezan con el segundo caracter de la primera palabra del texto
# (en minúscula o en mayúscula). Por ejemplo, en el texto:
# "Para el alfil no hay alcance." hay dos palabras ("alfil" y "alcance") que cumplen con la condición.

# 4 - Determinar la cantidad de palabras que contienen la expresión "pa" o "pA" (la "p" en minúscula) pero
# # de forma que la palabra no termine con esa expresión. Por ejemplo en el texto:
# # "Se paran y se sacan la capA para no tener frío en casa de Pablo.“, hay 2 palabras que cumplen con la condición:
# "paran" y "para". La palabra "Pablo" no cuenta porque la "P" está en mayúscula, y la palabra "capA"
# tiene la secuencia pedida, pero no cuenta porque la palabra termina ella.

def es_vocal(letra):
    return letra in "aeiouáéíóúAEIUOÁÉÍÓÚ"


def principal():
    cont_letras_palabra = 0
    cont_palabrasp1 = 0
    cont_vocales = 0
    cont_palabrasp2 = 0
    cont_palabrasp3 = 0
    cont_palabrasp4 = 0
    pos_ult_let = 0
    posc_a = 0
    cumple_p3 = False
    cont_palabras_general = 0
    hay_qz = False
    sec_let = ult_car = None
    seg_let_pri = pri_let = None
    hay_p = False
    hay_pa = False
    texto = input("Ingrese su texto: ")

    for car in texto:
        if car != " " and car != ".":

            if cont_letras_palabra == 0:
                pri_let = car

            cont_letras_palabra += 1
            if es_vocal(car):
                cont_vocales += 1

            if car == "q" or car == "z" or car == "Q" or car == "Z":
                hay_qz = True

            if cont_letras_palabra == 2:
                sec_let = car
            if cont_palabras_general == 0:
                seg_let_pri = sec_let

            elif seg_let_pri == pri_let:
                cumple_p3 = True
            if car == "p":
                hay_p = True
            elif hay_p:
                if car == "a" or car == "A":
                    hay_pa = True
                    posc_a = cont_letras_palabra

                else:
                    hay_p = False
            ult_car = car
            pos_ult_let = cont_letras_palabra

        else:
            ult_car = ult_car.lower()
            sec_let = sec_let.lower()
            if cumple_p3 and cont_letras_palabra > 2:
                cont_palabrasp3 += 1
            cont_palabras_general += 1
            if sec_let == ult_car:
                cont_palabrasp2 += 1
            if cont_vocales >= 2 and not hay_qz:
                cont_palabrasp1 += 1
            if hay_pa and posc_a != pos_ult_let:
                cont_palabrasp4 += 1

            cont_letras_palabra = 0
            cont_vocales = 0
            cumple_p3 = False
            hay_pa = hay_p = False

    print(cont_palabrasp1)
    print(cont_palabrasp2)
    print(cont_palabrasp3)
    print(cont_palabrasp4)


if __name__ == "__main__":
    principal()
