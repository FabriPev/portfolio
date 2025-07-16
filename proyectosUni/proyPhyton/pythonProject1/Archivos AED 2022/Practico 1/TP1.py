import random
# Datos:

fig1 = False
# # Bienvenida:
print("¡El juego del Blackjack!")
print(" ")

# # Nombre del jugador:
jugador = input("Ingresa el nombre del jugador: ")

# Comienzo de mano:
print(" ")
print("¡¡Empieza el juego!!")

# # Números y palos:
palo = "Tréboles", "Diamantes", "Corazones", "Picas"
numeros = "A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"
figuras = "A", "J", "Q", "K"

# # Mano:
# # Cartas del jugador:
print("=" * 121)
print("Cartas de", jugador, ": ")
c1_jugador = random.choice(numeros), random.choice(palo)
c2_jugador = random.choice(numeros), random.choice(palo)
print("Carta Nº 1: ", c1_jugador)
print("Carta Nº 2: ", c2_jugador)

# # Cartas del crupier:
print("-" * 121)
print("Cartas del Crupier: ")
c1_crupier = random.choice(numeros), random.choice(palo)
c2_crupier = random.choice(numeros), random.choice(palo)
print("Carta Nº 1: ", c1_crupier)
print("Carta Nº 2: ", c2_crupier)

# Procesos
# # Puntaje parcial jugador y cálculo de figuras:
puntaje_parcial_jugador = 0
if c1_jugador[0] == "J" or c1_jugador[0] == "Q" or c1_jugador[0] == "K":
    puntaje_parcial_jugador += 10
    fig1 = True
elif c1_jugador[0] == "A":
    puntaje_parcial_jugador += 11
    fig1 = True
else:
    puntaje_parcial_jugador += c1_jugador[0]

if c2_jugador[0] == "J" or c2_jugador[0] == "Q" or c2_jugador[0] == "K":
    puntaje_parcial_jugador += 10
    fig1 = True
elif c2_jugador[0] == "A" and (puntaje_parcial_jugador + 11) <= 21:
    puntaje_parcial_jugador += 11
    fig1 = True
elif c2_jugador[0] == "A" and (puntaje_parcial_jugador + 11) > 21:
    puntaje_parcial_jugador += 1
    fig1 = True
else:
    puntaje_parcial_jugador += c2_jugador[0]
print("=" * 121)
print("Puntaje parcial de", jugador, ": ", puntaje_parcial_jugador)

# # Puntaje parcial crupier:
puntaje_parcial_crupier = 0

if c1_crupier[0] == "J" or c1_crupier[0] == "Q" or c1_crupier[0] == "K":
    puntaje_parcial_crupier += 10
    fig1 = True
elif c1_crupier[0] == "A":
    puntaje_parcial_crupier += 11
    fig1 = True
else:
    puntaje_parcial_crupier += c1_crupier[0]

if c2_crupier[0] == "J" or c2_crupier[0] == "Q" or c2_crupier[0] == "K":
    puntaje_parcial_crupier += 10
    fig1 = True
elif c2_crupier[0] == "A" and (puntaje_parcial_crupier + 11) <= 21:
    puntaje_parcial_crupier += 11
    fig1 = True
elif c2_crupier[0] == "A" and (puntaje_parcial_crupier + 11) > 21:
    puntaje_parcial_crupier += 1
    fig1 = True
else:
    puntaje_parcial_crupier += c2_crupier[0]
print("-" * 121)
print("Puntaje parcial del crupier: ", puntaje_parcial_crupier)

# # Cálculo de tercer carta jugador:
if puntaje_parcial_jugador <= 16:
    c3_jugador = random.choice(numeros), random.choice(palo)
    print("=" * 121)
    print("Carta Nº 3 de", jugador, ": ", c3_jugador)
    if c3_jugador[0] == "J" or c3_jugador[0] == "Q" or c3_jugador[0] == "K":
        puntaje_parcial_jugador += 10
        fig1 = True
    elif c3_jugador[0] == "A" and (puntaje_parcial_jugador + 11) <= 21:
        puntaje_parcial_jugador += 11
        fig1 = True
    elif c3_jugador[0] == "A" and (puntaje_parcial_jugador + 11) > 21:
        puntaje_parcial_jugador += 1
        fig1 = True
    else:
        puntaje_parcial_jugador += c3_jugador[0]
    puntaje_final_jugador = puntaje_parcial_jugador
else:
    puntaje_final_jugador = puntaje_parcial_jugador

# # Cálculo de tercer carta crupier:
if puntaje_parcial_crupier <= 16:
    c3_crupier = random.choice(numeros), random.choice(palo)
    print("-" * 121)
    print("Carta Nº 3 del crupier: ", c3_crupier)
    if c3_crupier[0] == "J" or c3_crupier[0] == "Q" or c3_crupier[0] == "K":
        puntaje_parcial_crupier += 10
        fig1 = True
    elif c3_crupier[0] == "A" and (puntaje_parcial_crupier + 11) <= 21:
        puntaje_parcial_crupier += 11
        fig1 = True
    elif c3_crupier[0] == "A" and (puntaje_parcial_crupier + 11) > 21:
        puntaje_parcial_crupier += 1
        fig1 = True
    else:
        puntaje_parcial_crupier += c3_crupier[0]
    puntaje_final_crupier = puntaje_parcial_crupier
else:
    puntaje_final_crupier = puntaje_parcial_crupier

# Resultados:
# # Puntaje final y cálculo de ganador:
print("=" * 121)
print("Puntaje final de", jugador, ": ", puntaje_final_jugador)
print("-" * 121)
print("Puntaje final del crupier: ", puntaje_final_crupier)
print("*" * 121)
if puntaje_final_jugador > 21 >= puntaje_final_crupier:
    print(jugador, " se pasó de 21.")
    print("Ganador: ¡Crupier!")
elif puntaje_final_crupier > 21 >= puntaje_final_jugador:
    print("El crupier se pasó de 21.")
    print("Ganador: ", "¡", jugador, "!")
elif puntaje_final_jugador > 21 and puntaje_final_crupier > 21:
    print("Ambos se pasaron de 21. ¡Es un empate!")
elif puntaje_final_jugador > puntaje_final_crupier:
    print("Ganador:", "¡", jugador, "!")
elif puntaje_final_crupier > puntaje_final_jugador:
    print("Ganador: ¡Crupier!")
else:
    print("¡Es un empate!")

# # Determinación de palo, número y figura:
if c1_jugador[1] == c1_crupier[1]:
    print("La primera carta de ", jugador, " y del crupier tienen el mismo palo.")
elif c1_jugador[1] == c1_crupier and c1_jugador[0] == c1_crupier[0]:
    print("La primera carta de", jugador, " y del crupier son iguales!")
if fig1:
    print("Salío al menos una figura en las cartas.")
# # Fin del juego
print("Fin del juego...")
