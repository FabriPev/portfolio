def es_num_impar(car):
    return car in "13579"

def consonates_mayusculas(car):
    return car in "QWRTYPSDFGHJKLÑZXCVBNM"

def tiene_vocal(car):
    return car in "aeiouáéíóúAEIOUÁÉÍÓÚ"

def porcentaje(total, parcial):
    porc = 0
    if total != 0:
        porc = parcial * 100 / total
    return porc

def principal ():
    # contadores
    # contador de caracteres...
    cl = 0
    r1, r2, r3, r4 = 0, None, 0, 0
    palabras = 0

    # contadores punto 1...
    tiene_impar= False
    tiene_cons_mayuscula = False

    # contadores punto 2..
    comienza_vocal = False

    #contradores punto 3...
    tiene_a = 0
    tiene_e = 0
    csa = 0


    #contadores punto 4...
    sdi = 0
    anterior = " "
    tiene_d = False

    m= open("entrada.txt")
    texto = m.read()
    m.close()

    #texto= "Las esperas nunca acaban."

    for car in texto:
        if car == " " or car == ".":
            if cl > 0:
                palabras += 1
                # resultado punto 1...
                if cl == tiene_impar + tiene_cons_mayuscula:
                    r1 += 1

                # resultado punto 2...
                if comienza_vocal and (r2 is None or cl < r2):
                    r2 = cl

                #resultado punto 3...
                if tiene_a > tiene_e:
                    csa += 1

                #resultado punto 4 ...
                if sdi >= 2 and tiene_vocal(anterior):
                    r4 += 1

                # reseteo...
                cl = 0
                tiene_impar = 0
                tiene_cons_mayuscula = 0
                comienza_vocal = False
                tiene_a = 0
                tiene_e = 0
                sdi = 0
                tiene_d = False

        else:
            cl += 1
            # punto 1...
            if es_num_impar(car):
                tiene_impar += 1
            elif consonates_mayusculas(car):
                tiene_cons_mayuscula += 1

            # punto 2...
            if cl == 1 and tiene_vocal(car):
                comienza_vocal = True

            # punto 3...
            if car == "a" or car == "á" or car == "A" or car == "Á":
                    tiene_a += 1
            elif car == "e" or car == "é" or car == "E" or car == "É":
                    tiene_e += 1

            #punto 4...
            if car == "d" or car == "D":
                    tiene_d += True
            else:
                if tiene_d and (car == "i" or car == "í" or car == "I" or car == "Í"):
                    sdi += 1
            anterior = car




    r3 = porcentaje(palabras,csa)

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)

if __name__ == '__main__':
    principal()