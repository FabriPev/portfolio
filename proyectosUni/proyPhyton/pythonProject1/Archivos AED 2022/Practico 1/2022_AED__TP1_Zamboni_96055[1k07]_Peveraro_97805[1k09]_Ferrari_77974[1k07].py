import random

print("-" * 36)
print("¡Bienvenido al BlackJack!")
print("-" * 36)

nmb = input("Ingrese su nombre para iniciar: ")

palos = "♠", "♥", "♣", "♦"
valores = "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"

# Las dos variables anteriores son tuplas para definir las cartas

figuras_player = False
cantidad_figuras_player = 0

# Utilizamos esto para la última consigna que nos pide determinar si hay figuras en el mazo del jugador


figuras_croupier = False
cantidad_figuras_croupier = 0

# Con esto veremos si al croupier le han salido figuras

paloplayer1 = random.choice(palos)
valorplayer1 = random.choice(valores)

valorplayer = valorplayer1

# Guardamos esta variable para luego hacer la comparación

print(nmb, "tu primera carta es:", valorplayer1, paloplayer1)
# Ponemos este print antes de asignar valoras a J, Q, K Y A porque si no
# El valor mostrado sale como numero y no como figura

if valorplayer1 == "A":
    valorplayer1 = 11
elif valorplayer1 == "J" or valorplayer1 == "Q" or valorplayer1 == "K":
    valorplayer1 = 10
    figuras_player = True
    cantidad_figuras_player = cantidad_figuras_player + 1

a = input("\nPulse enter para continuar")

paloplayer2 = random.choice(palos)
valorplayer2 = random.choice(valores)

print(nmb, "tu segunda carta es:", valorplayer2, paloplayer2)

if valorplayer2 == "A" and valorplayer1 <= 10:
    valorplayer2 = 11
elif valorplayer2 == "A":
    valorplayer2 = 1

if valorplayer2 == "J" or valorplayer2 == "Q" or valorplayer2 == "K":
    valorplayer2 = 10
    figuras_player = True
    cantidad_figuras_player = cantidad_figuras_player + 1

valor_total_player = valorplayer1 + valorplayer2

print(nmb, "tu puntaje parcial es de: ", valor_total_player)

a = input("\nPulse enter para continuar")

crupiervalor1 = random.choice(valores)
crupierpalos1 = random.choice(palos)

valorcrupier = crupiervalor1

print("\nLa primera carta del croupier ha sido:", crupiervalor1, crupierpalos1)

if valorplayer1 == "A":
    valorplayer1 = 11
elif valorplayer1 == "J" or valorplayer1 == "Q" or valorplayer1 == "K":
    valorplayer1 = 10
    figuras_player = True
    cantidad_figuras_player = cantidad_figuras_player + 1

if crupiervalor1 == "A":
    crupiervalor1 = 11
elif crupiervalor1 == "J" or crupiervalor1 == "Q" or crupiervalor1 == "K":
    crupiervalor1 = 10
    figuras_croupier = True
    cantidad_figuras_croupier += 1

# Con esto cambiamos los valores de A, J, Q Y K, y los trasformamos a valores de int

a = input("\nPulse enter para continuar")

croupierpalo2 = random.choice(palos)
croupiervalor2 = random.choice(valores)

print("La segunda carta del croupier es: ", croupiervalor2, croupierpalo2)

if croupiervalor2 == "A" and crupiervalor1 <= 10:
    croupiervalor2 = 11
elif croupiervalor2 == "A":
    croupiervalor2 = 1

if croupiervalor2 == "J" or croupiervalor2 == "Q" or croupiervalor2 == "K":
    croupiervalor2 = 10
    figuras_croupier = True
    cantidad_figuras_croupier = cantidad_figuras_croupier + 1

total_croupier = crupiervalor1 + croupiervalor2

print("El total parcial del croupier es de: ", total_croupier)

input("\nPulse enter para continuar")

valorplayer3 = 0
if valor_total_player < 19:
    # vamos a hacer que si tiene 19 se plante,
    # ya que es muy probable que se pase de 21 y pierda
    paloplayer3 = random.choice(palos)
    valorplayer3 = random.choice(valores)
    print(nmb, "tu tercer carta es:", valorplayer3, paloplayer3)
    if valorplayer3 == "A" and valor_total_player <= 10:
        valorplayer3 = 11
    elif valorplayer3 == "A":
        valorplayer3 = 1
    if valorplayer3 == "J" or valorplayer3 == "Q" or valorplayer3 == "K":
        valorplayer3 = 10
        figuras_player = True
        cantidad_figuras_player = cantidad_figuras_player + 1

valor_total_player = valorplayer1 + valorplayer2 + valorplayer3

print(nmb, "tu puntaje total es de:", valor_total_player)

input("\n Pulse enter para continuar")

croupiervalor3 = 0
if total_croupier < 17:  # vamos a hacer que si tiene 17 se plante, ya que es una norma en el juego
    croupierpalos3 = random.choice(palos)
    croupiervalor3 = random.choice(valores)
    print("La tercera carta del croupier es:", croupiervalor3, croupierpalos3)
    if croupiervalor3 == "A" and total_croupier <= 10:
        croupiervalor3 = 11
    elif croupiervalor3 == "A":
        croupiervalor3 = 1
    if croupiervalor3 == "J" or croupiervalor3 == "Q" or croupiervalor3 == "K":
        croupiervalor3 = 10
        figuras_croupier = True
        cantidad_figuras_croupier = cantidad_figuras_croupier + 1

total_croupier = crupiervalor1 + croupiervalor2 + croupiervalor3

print("El puntaje total del croupier es de:", total_croupier)

input("\n Pulse enter para continuar")

# Resultados y se determina al ganador

print("-" * 36)

if total_croupier < valor_total_player <= 21:
    print("¡FELICIDADES", nmb, "HAS GANADO<3!")
else:
    if valor_total_player < total_croupier <= 21:
        print("El croupier ha ganado,", nmb, "has perdido :(")
    else:
        if total_croupier == valor_total_player:
            print("Es un empate, ambos jugadores han obtenido el mismo puntaje")
        else:
            if total_croupier > 21 and valor_total_player > 21:
                print("Es un empate, ambos han perdido")
            else:
                if total_croupier > 21 >= valor_total_player:
                    print("¡FELICIDADES", nmb, "HAS GANADO<3!")
                elif valor_total_player > 21 >= total_croupier:
                    print("El croupier ha ganado,", nmb, "has perdido :(")

print("-" * 36)

print("")
# Ahora vamos con las resoluciones extras
ambos_palos = False
if paloplayer1 == crupierpalos1:
    print("Ambos jugadores tuvieron el mismo palo en su primera carta")
    ambos_palos = True

if ambos_palos and valorplayer == valorcrupier:
    print("¡WOW! No solo han coincidido en palo, sino también en el numero!")

figuras_totales = cantidad_figuras_croupier + cantidad_figuras_player

if cantidad_figuras_croupier or cantidad_figuras_player > 0:
    print(nmb, "tuvo un total de :", cantidad_figuras_player, "figuras")
    print("EL Croupier tuvo un total de:", cantidad_figuras_croupier, "figuras")
    print("Es decir hubo un total de:", figuras_totales, "figuras")

print("El juego ha terminado, ¡Gracias por jugar!")
