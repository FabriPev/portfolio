def es_digito_impar(car):
    return car in "13579"


def es_consonante_mayuscula(car):
    return car in "BCDFGHJKLMNÑPQRSTVWXYZ"


def es_vocal(car):
    return car.lower() in "aeiouáéíóúü"


def porcentaje(total, parcial):
    porc = 0
    if total != 0:
        porc = parcial * 100 / total
    return porc


def principal():
    # Inicializar variables de resultados...
    r1 = r3 = r4 = r5 = 0
    r2 = None

    # contador de caracteres de una palabra y contador de palabras...
    cl = cp = 0

    # contadores para el resultado r1...
    cdi = ccm = 0

    # flags para el resultado r2...
    iv = False

    # contadores para el resultado r3...
    cla = cle = cpae = 0

    # contadores y flags para el resultado r4...
    sd, csdi, ant = False, 0, ""

    # contadores y auxiliares para r5...
    pos = 0

    # m = open("entrada.txt")
    # texto = m.read()
    # m.close()

    texto = "La clave 1alfaxy puede funcionar en lugar de 1beta9 o en lugar de 9sigmaZ. Las cosas comienzan a volverse extremadamente negras. Secos los pozos entre tantas mejoras. Se nota la esencia pese al segundo tiempo El lugar marcado como X31F57 es conocido también como X23A54 Antes de esa esperada circunstancia era imposible hg3djh jui8 3ko4 5 uj6ui Las esperas nunca acaban Didide didida dijo el cantor."

    for car in texto:
        if car in " .":
            # fin de palabra...

            # procesar la palabra solo si el contador de letras era mayor a cero...
            if cl > 0:

                # contar una palabra (Resultado 3)...
                cp += 1

                # Resultado r1...
                if cl == cdi + ccm:
                    r1 += 1

                # Resultado r2...
                if iv and (r2 is None or cl < r2):
                    r2 = cl

                # Resultado 3...
                if cla > cle:
                    cpae += 1

                # Resultado 4...
                if csdi >= 2 and es_vocal(ant):
                    r4 += 1

                # Resultado 5...
                if 0 < pos <= cl // 2:
                    r5 += 1

                # Resetear contadores y flags...
                cl = 0

                # para r1...
                cdi = ccm = 0

                # para r2...
                iv = False

                # para r3...
                cla = cle = 0

                # para r4...
                sd, csdi = False, 0

                # para r5...
                pos = 0

        else:
            # dentro de la palabra....
            # contar todas los caracteres de la palabra actual...
            cl += 1

            # Resultado r1...
            if es_digito_impar(car):
                cdi += 1
            elif es_consonante_mayuscula(car):
                ccm += 1

            # Resultado 2...
            if cl == 1 and es_vocal(car):
                iv = True

            # Resultado 3...
            if car in "aáAÁ":
                cla += 1
            elif car in "eéEÉ":
                cle += 1

            # Resultado 4...
            if car in "dD":
                sd = True
            else:
                if sd and car in "iíIÍ":
                    csdi += 1
                sd = False

            # nos quedamos con la letra anterior...
            ant = car

            # Resultado r5...
            if car.isdigit() and pos == 0:
                pos = cl


    # Porcentaje para r3...
    r3 = porcentaje(cp, cpae)

    # Visualización de resultados...
    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)
    print("Quinto resultado:", r5)


if __name__ == '__main__':
    principal()