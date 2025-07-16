wimport random


def inicio():  # Utilizamos esta ffuncion para dar inicio al programa
    print("-" * 36)
    nombre = input("Ingrese su nombre: ")
    plata = int(input("Ingrese cual quiere que sea su pozo: "))
    print("-" * 36)
    while plata < 0 or plata > 100000:
        print("Cantidad de pozo no valida")
        plata = int(input("Ingrese cual quiere que sea su pozo: "))
    return nombre, plata


def que_hago():  # Utilizamos esta funcion para cada vez que el
    # usuario tenga la oportunidad de decidir que hacer
    print("-" * 36)
    elijo = int(input(menu))
    print("-" * 36)
    return elijo


def generar_cartas(puntaje):  # Funcion para generar cartas
    palos = "♠", "♥", "♣", "♦"
    valor = random.randint(1, 13)
    palo_carta = random.choice(palos)

    if (valor > 1) and (valor < 11):
        nombre_carta = valor
        puntos = valor
    else:
        if valor == 1:
            nombre_carta = 'AS'
            if puntaje <= 10:
                puntos = 11
            else:
                puntos = 1
        else:
            puntos = 10
            if valor == 11:
                nombre_carta = 'J'
            elif valor == 12:
                nombre_carta = 'Q'
            else:
                nombre_carta = 'K'

    return nombre_carta, palo_carta, puntos


def apuesta(a_apostar, accion, n_ronda, aposto):
    n_ronda += 1
    cant_apostf = 0
    opf = -1
    if a_apostar == 0:
        print("Su pozo ha quedado en 0, salga y vuelva a entrar para seguir jugando")
    while cant_apostf == 0:
        if a_apostar < 5:
            print("No puede apostar ahora")
            opf = que_hago()
        if cant_apostf == 0:
            cant_apostf = int(input("Cuanto desea apostar: "))
        if cant_apostf % 5 != 0 or cant_apostf <= 0 or cant_apostf > a_apostar:
            cant_apostf = int(input("Cantidad no valida, Cuanto desea apostar: "))
        if cant_apostf % 5 == 0 and cant_apostf > a_apostar:
            cant_apostf = int(input("Cantidad no valida, Cuanto desea apostar: "))
        if cant_apostf % 5 == 0 and cant_apostf != 0:
            aposto += cant_apostf
            opf = que_hago()
            accion = True
        a_apostar -= cant_apostf
    return cant_apostf, opf, a_apostar, accion, n_ronda, aposto


def ganador(puntaje1, cartas1, puntaje2, cartas2, bljkn):  # gj, gana jugador, gc- gana croupier, e, empate
    gj = 0
    gc = 1   # Vamos a utilizar 0, 1 y 2 para determinar a los ganadores ya que nos simplifica a la hora del retorno
    e = 2

    if puntaje1 < 21 and puntaje2 < 21:
        if puntaje1 > puntaje2:
            return gj, bljkn
        elif puntaje2 > puntaje1:
            return gc, bljkn
        else:
            return e, bljkn
    elif puntaje1 == 21 and puntaje2 != 21:
        return gj, bljkn
    elif puntaje2 == 21 and puntaje1 != 21:
        return gc, bljkn
    elif puntaje1 > 21 and puntaje2 > 21:
        return gc, bljkn
    elif puntaje1 > 21 and puntaje2 < 21:
        return gc, bljkn
    elif puntaje1 < 21 and puntaje2 > 21:
        return gj, bljkn
    elif puntaje1 == 21 and puntaje2 == 21:

        if cartas1 == 2 and cartas2 > 2:
            bljkn = 1
            return gj, bljkn
        elif cartas1 > 2 and cartas2 == 2:
            bljkn = 1
            return gc, bljkn
        elif cartas1 == 2 and cartas2 == 2:
            bljkn = 1
            return e, bljkn
        else:
            return e, bljkn
    elif puntaje1 <= 21 and puntaje2 > 21:
        return gj, bljkn
    else:
        return e, bljkn


def result_apuesta(winner, cant_de_apuesta, billetera, accion, gan_jugador, racha):
    perdida = 0
    if winner == 0:
        print("Felicidades, ", nmb, "has ganado!!")
        previo = (cant_de_apuesta * 2)
        billetera += previo
        cant_de_apuesta = 0
        gan_jugador += 1
        accion = False
        racha = 0
    elif winner == 1:
        print("¡El croupier ha ganado!")
        billetera = billetera
        perdida = cant_de_apuesta
        cant_de_apuesta = 0
        accion = False
        while winner == 1:
            racha += 1
            break
    elif winner == 2:
        print("¡Es un empate!")
        billetera += cant_de_apuesta
        cant_de_apuesta = 0
        accion = False
        racha = 0

    return gana, cant_de_apuesta, billetera, accion, gan_jugador, racha, perdida


def maximo(comp, ant_max):  # Al tener varios maximos a definir usamos esta funcion simple para hacerlo
    if comp > ant_max:
        ant_max = comp
    else:
        ant_max = ant_max
    return ant_max


def fin(nombre, por_vic, rach_vic, bljkm, max_pot, perdida_grande, media_apost):
    print("Felicidades ", nombre, "tu porcentaje de victores es del: ", por_vic, "%")
    print("La mayor racha de victorias del croupier fue de: ", rach_vic, "rondas")
    print("En la partido hubo en total de ", bljkm, "rondas con al menos un blackjack natural")
    print("Tu maximo pozo alcanzado fue de: ", max_pot)
    print("El monto promedio de las apuestas realizadas fue de: ", media_apost)
    print("Tu maxima perdida fue de: ", perdida_grande)
    print("¡Gracias por jugar!, vuelva a iniciar el programa para volver a jugar")


nmb, pozo = inicio()
first_pot = pozo
menu = "¡Bienvenido al juego de BlackJack!\n" \
       "Seleccione una opción : \n" \
       "1 - Apostar \n" \
       "2 - Jugar una mano\n" \
       "3 - Salir\n" \
       "Seleccione su opción: "
op = -1
dinero = False
ult_max = max_lost = tot_apuesta = mejor_racha_c = 0
max_pozo = first_pot
cant_apost = 0
rondas_jugadas = vic_jugador = racha_c = manobljk = 0

while op != 3:
    op = que_hago()
    while op == 1 and not dinero:
        cant_apost, op, pozo, dinero, rondas_jugadas, tot_apuesta = apuesta(pozo, dinero, rondas_jugadas, tot_apuesta)
    while op == 1 and dinero:
        print("Ya ha habido una apuesta, comience el juego")
        op = que_hago()
    while op == 2:

        while not dinero or cant_apost % 5 != 0:
            print("Error en la apuesta, vuelva a apostar")
            cant_apost, op, pozo, dinero, rondas_jugadas, tot_apuesta\
                = apuesta(pozo, dinero, rondas_jugadas, tot_apuesta)
        hubo_bljckn = 0
        puntajej = 0
        carta1j, palo1j, punto1j = generar_cartas(puntajej)
        puntajej += punto1j
        carta2j, palo2j, punto2j = generar_cartas(puntajej)
        print("Tu pozo inicial fue de: ", first_pot)
        print("Tu apuesta es de: ", cant_apost)
        print(nmb, "tu primera carta es: ", carta1j, palo1j)
        print(nmb, "tu segunda carta es: ", carta2j, palo2j)
        cantcarj = 2
        puntajej += punto2j
        print(nmb, "Tu puntaje hasta ahora es: ", puntajej)
        puntajec = 0
        carta1c, palo1c, punto1c = generar_cartas(puntajec)
        puntajec += punto1c
        print("La primera carta del croupier es:", carta1c, palo1c)
        cantcarc = 1
        print("El puntaje del croupier es: ", puntajec)
        while puntajej < 21:
            aff = input("Desea una nueva carta?(Respondo con Si o No): ")
            if aff == "Si":
                carta3j, palo3j, punto3j = generar_cartas(puntajej)
                print(nmb, "Tu nueva carta es: ", carta3j, palo3j)
                puntajej += punto3j
                print("Tu puntaje es: ", puntajej)
                cantcarj += 1
            else:
                break

        while puntajec < 17:
            carta3c, palo3c, punto3c = generar_cartas(puntajec)
            print("La nueva carta del croupier es: ", carta3c, palo3c)
            puntajec += punto3c
            print("El nuevo puntaje del croupier es: ", puntajec)
            cantcarc += 1
        gana, hubo_bljckn = ganador(puntajej, cantcarj, puntajec, cantcarc, hubo_bljckn)
        if hubo_bljckn == 1:
            manobljk += 1
        gana, cant_apost, pozo, dinero, vic_jugador, racha_c, big_lose \
            = result_apuesta(gana, cant_apost, pozo, dinero, vic_jugador, racha_c)
        print("Tu nuevo pozo total es de: ", pozo)

        ult_max = maximo(racha_c, ult_max)
        max_pozo = maximo(pozo, max_pozo)
        max_lost = max(big_lose, max_lost)
        break

while op == 3:
    porc_vic_jug = (vic_jugador * 100) // rondas_jugadas
    prom_apost = tot_apuesta // rondas_jugadas
    fin(nmb, porc_vic_jug, ult_max, manobljk, max_pozo, max_lost, prom_apost)
    break
