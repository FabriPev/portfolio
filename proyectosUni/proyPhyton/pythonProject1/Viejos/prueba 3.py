def hay_digito(letra):
    if "0" <= letra <= "9":
        return True
    else:
        return False


def porc(contador_parcial, contador_total):
    porcentaje = (contador_parcial * 100) // contador_total
    return porcentaje


def tipo_letra(letra):
    return letra in "aeiou"


def compa(a_comparar, og):
    if a_comparar == og:
        return True
    else:
        return False


def principal():
    texto = input('Ingrese un texto(finaliza con punto): ')
    texto = texto.lower()
    # Banderas:
    hubo_k_r = False
    hubo_s = False
    hubo_se = False
    # Contadores:
    cont_digitos = 0
    cant_pal_1 = 0
    cont_pal_total_2 = 0
    mayor_consonant = 0
    vocal = consonant = 0
    # Punto 3:
    cont_let = 0
    cont_let_pal = 0
    repi_pri_let = 0
        #Punto 4
    se_palabra = 0
    for car in texto:
        if car != " " and car != ".":
            cont_let += 1
            cont_let_pal += 1
            if hay_digito(car):
                cont_digitos += 1
            else:
                if car == "k" or car == "r":
                    hubo_k_r = True
            if tipo_letra(car) == True:
                vocal += 1
            else:

                consonant += 1
            if cont_let == 1:
                primera_l = car
            if cont_let_pal <= 3:

                if compa(car, primera_l) == True:
                    repi_pri_let += 1
            if cont_let_pal > 1:
                if hubo_s == True:
                    if car == "e":
                        hubo_se = True
                    else:
                        hubo_s = False
                if car == "s":
                    hubo_s = True

        else:
            cont_pal_total_2 += 1
            if consonant > vocal:
                mayor_consonant += 1

            if cont_digitos > 2 and hubo_k_r == True:
                cant_pal_1 += 1
            if hubo_se == True:
                se_palabra += 1
            # Reiniciamos:
            cont_digitos = 0
            hubo_k_r = False
            vocal = consonant = 0
            cont_let_pal = 0
            hubo_s = False
            hubo_se = False

    por_2 = porc(mayor_consonant, cont_pal_total_2)
    print("punto 1, ", cant_pal_1)
    print("punto 2, ", por_2)
    print("punto 3, ", repi_pri_let)
    print("punto 4, ", se_palabra)


principal()

