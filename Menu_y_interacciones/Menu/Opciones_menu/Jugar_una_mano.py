from Generadores.generar_cartas import generador_1
from Menu_y_interacciones.Menu.menu_opciones import menu_opciones

def jugar_una_mano(monto_pozo_actual):
    monto_apostado = 0
    desicion_jugador = 1
    puntaje_actual_jugador = 0
    puntaje_actual_croupier = 0

    print("ingrese el valor a apostar")
    monto_apostado = int(input())

    if monto_apostado <= monto_pozo_actual and monto_apostado % 5 == 0 and monto_pozo_actual >= 5:

        nombre_carta_jugador_1, palo_carta_jugador_1, carta_jugador_1  = generador_1()

        carta_jugador_1_tupla = (nombre_carta_jugador_1, palo_carta_jugador_1)

        nombre_carta_jugador_2, palo_carta_jugador_2, carta_jugador_2 = generador_1()

        carta_jugador_2_tupla = (nombre_carta_jugador_2, palo_carta_jugador_2)

        nombre_carta_croupier_1, palo_carta_croupier_1, carta_croupier_1 = generador_1()

        carta_croupier_1_tupla = (nombre_carta_croupier_1, palo_carta_croupier_1)

        puntaje_actual_jugador = carta_croupier_1 + carta_jugador_2

        puntaje_actual_croupier = carta_croupier_1

        print(carta_jugador_1_tupla, "Tercera carta jugador")
        print(carta_jugador_2_tupla, "Segunda carta jugador")
        print(carta_croupier_1_tupla,"primera carta croupier")
        print(puntaje_actual_jugador)
        print(puntaje_actual_croupier)

        while puntaje_actual_jugador < 21 and desicion_jugador == 1:
            desicion_jugador = int(input("Si desea pedir otra carta preciones 1, si desea plantarse precione 2"))
            if desicion_jugador == 1:
                 nombre_carta_jugador, palo_carta_jugador, carta_jugador = generador_1()

        puntaje_final_jugador = puntaje_actual_jugador
        print("Su puntaje final es: ", puntaje_final_jugador)

    else:
        menu_opciones()
