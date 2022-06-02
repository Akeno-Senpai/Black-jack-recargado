

def jugar_una_mano(monto_pozo_actual, monto_pozo_inicial):

    from Juego.Cuerpo_del_juego.Analisis_resultados.Resultados_ronda import Resultado

    from Generadores.generar_cartas import generador_1

    import time

    monto_apostado = 0

    desicion_jugador = 1

    puntaje_actual_jugador = 0

    puntaje_actual_croupier = 0

    print("\n", "ingrese el valor a apostar:")

    print("")

    monto_apostado = int(input("\n\t"))

    print("º" * 100)

    print("º" * 100)

    if monto_pozo_actual == 0:
        monto_pozo_actual = monto_pozo_inicial

    if monto_apostado <= monto_pozo_actual and monto_apostado % 5 == 0 and monto_pozo_actual >= 5:

        nombre_carta_jugador_1, palo_carta_jugador_1, carta_jugador_1  = generador_1()

        carta_jugador_1_tupla = (nombre_carta_jugador_1, palo_carta_jugador_1)

        nombre_carta_jugador_2, palo_carta_jugador_2, carta_jugador_2 = generador_1()

        carta_jugador_2_tupla = (nombre_carta_jugador_2, palo_carta_jugador_2)

        nombre_carta_croupier_1, palo_carta_croupier_1, carta_croupier_1 = generador_1()

        carta_croupier_1_tupla = (nombre_carta_croupier_1, palo_carta_croupier_1)

        nombre_carta_croupier_2, palo_carta_croupier_2, carta_croupier_2 = generador_1()

        carta_croupier_2_tupla = (nombre_carta_croupier_2, palo_carta_croupier_2)

        puntaje_actual_jugador = carta_jugador_1 + carta_jugador_2

        puntaje_actual_croupier = carta_croupier_1

        print("\n", carta_jugador_1_tupla, "Primera carta jugador")

        print("\n", carta_jugador_2_tupla, "Segunda carta jugador")

        print("")

        print("º" * 100)

        print("º" * 100)

        print("\n", carta_croupier_1_tupla,"Primera carta croupier")

        print("")

        print("º" * 100)

        print("º" * 100)

        print("\n", puntaje_actual_jugador, "Puntaje total actual jugador")

        print("\n", puntaje_actual_croupier, "Puntaje total actual croupier")

        print("")

        print("º" * 100)

        print("º" * 100)

        while puntaje_actual_jugador < 21 and desicion_jugador == 1:

            print("\n", "Seleccione alguna de las siguientes opciones: ")

            print("\n", "1- Pedir otra carta")

            print("\n", "2- Plantarse")

            print("")

            print("º" * 100)

            print("º" * 100)

            decision_jugador = int(input())

            if decision_jugador == 1:

                nombre_carta_jugador, palo_carta_jugador, carta_jugador = generador_1()

                carta_jugador_tupla = (nombre_carta_jugador, palo_carta_jugador)

                puntaje_actual_jugador += carta_jugador

                print("\n", "Tu nueva carta es:", carta_jugador_tupla)

                print("\n", puntaje_actual_jugador, "Puntaje total actual jugador")

                print("º" * 100)

                print("º" * 100)

                while puntaje_actual_croupier < 21 and puntaje_actual_jugador >= 21:

                    nombre_carta_croupier, palo_carta_croupier, carta_croupier = generador_1()

                    carta_croupier_tupla = (nombre_carta_croupier, palo_carta_croupier)

                    print("\nLa nueva carta del croupier es: ", carta_croupier_tupla)

                    puntaje_actual_croupier += carta_croupier

                    print("\nPuntaje actual del croupier: ", puntaje_actual_croupier)

                    Resultado(puntaje_actual_jugador, puntaje_actual_croupier)

                    print("º" * 100)

                    print("º" * 100)

            elif decision_jugador == 2:

                puntaje_final_jugador = puntaje_actual_jugador

                print("\n", "El puntaje final del jugador es: ", puntaje_final_jugador)

                print(carta_croupier_2_tupla, "Segunda carta del croupier")

                puntaje_actual_croupier = carta_croupier_1 + carta_croupier_2

                while puntaje_actual_croupier < 21:

                    nombre_carta_croupier, palo_carta_croupier, carta_croupier = generador_1()

                    carta_croupier_tupla = (nombre_carta_croupier, palo_carta_croupier)

                    print("\nLa nueva carta del croupier es: ", carta_croupier_tupla)

                    puntaje_actual_croupier += carta_croupier

                    print("\nPuntaje actual del croupier: ", puntaje_actual_croupier)


                time.sleep(1)

                print("Verificando ganador de ronda")

                time.sleep(1)

                print("")

                print("º" * 100)

                print("º" * 100)

                print("º" * 100)

                print("º" * 100)

                print("º" * 100)

                print("º" * 100)

                Resultado(puntaje_actual_jugador, puntaje_actual_croupier)

            else:

                print("Lea bien las opciones, no sea pelotudo")

                time.sleep(1.5)

        if puntaje_actual_jugador > 21:

            puntaje_final_jugador = puntaje_actual_jugador

            puntaje_final_croupier = puntaje_actual_croupier

            print("\n", "El puntaje final del jugador es: ", puntaje_final_jugador)

            print("\n", "La mano ah finalizado, a continuacion sera redirijido al menu principal")

            time.sleep(1)

            print("Verificando ganador de ronda")

            time.sleep(1)

            print("")

            print("º" * 100)

            print("º" * 100)

            print("º" * 100)

            print("º" * 100)

            print("º" * 100)

            print("º" * 100)

            Resultado(puntaje_final_jugador, puntaje_final_croupier)

        if puntaje_actual_jugador == 21:

            puntaje_final_jugador = puntaje_actual_jugador

            puntaje_final_croupier = puntaje_actual_croupier

            print("\n", "El puntaje final del jugador es: ", puntaje_final_jugador)

            print("\n", "El puntaje final del croupier es: ", puntaje_final_croupier)

            print("\n", "La mano ah finalizado, a continuacion sera redirijido al menu principal")


            time.sleep(1)

            print("Verificando ganador de ronda")

            time.sleep(1)

            print("")

            print("º" * 100)

            print("º" * 100)

            print("º" * 100)

            print("º" * 100)

            print("º" * 100)

            print("º" * 100)

            Resultado(puntaje_final_jugador, puntaje_final_croupier)

