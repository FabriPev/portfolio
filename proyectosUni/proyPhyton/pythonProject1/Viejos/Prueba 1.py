def prom(numero_grande, numero_chico):
    promedio = numero_grande // numero_chico
    return promedio


def principal():
    n_word = us_cont = inicio_t = False
    hay_a = hay_s = hay_e = False
    hay_r = hay_re = False
    mas4let = re_palabra = 0
    texto = input("Ingrese su texto termianado en punto: ")
    texto = texto.lower()
    cant_let = t_letras = t_palabra = 0
    palabras_as = 0
    letra = "a"
    for cad in texto:

        if cad != " " and cad != ".":
            letra = cad
            cant_let += 1
            if cad == "n":
                n_word = True
            if cant_let > 4 and n_word and not us_cont:
                mas4let += 1
                us_cont = True
            if cad == "t" and cant_let == 1:
                inicio_t = True
            if inicio_t:
                t_letras += 1
            if cad == "a":
                hay_a = True
            if cad == "s":
                hay_s = True
            if cad == "e":
                hay_e = True
            if cad == "r":
                hay_r = True

            if hay_r:
                if cad == "e":
                    hay_re = True
                else:
                    hay_r = False
        else:
            if hay_re:
                if letra == "o":
                    re_palabra += 1
            if inicio_t:
                t_palabra += 1
            if hay_a and hay_s and hay_e == False:
                palabras_as += 1
            n_word = False
            cant_let = 0
            us_cont = False
            inicio_t = False
            hay_a = hay_s = hay_e = False
            hay_r = hay_re = False
        if cad == ".":
            t_promedio = prom(t_letras, t_palabra)
            print(mas4let)
            print(t_promedio)
            print(palabras_as)
            print(re_palabra)

if __name__ == '__main__':
    principal()
