

def jugar_una_mano(monto_pozo_actual, monto_pozo_inicial):

    from Juego.Cuerpo_del_juego.Analisis_resultados.Resultados_ronda import Resultado

    from Generadores.generar_cartas import generador_1

    from Generadores.analisis_AS import analisis_AS

    import time

    racha_croupier = 0

    victorias_jugador = 0

    partidas_jugadas = 0

    monto_apostado = 0

    desicion_jugador = 1

    puntaje_actual_jugador = 0

    puntaje_actual_croupier = 0

    print("-"*100)

    print("\n En tu pozo tienes disponible: ", monto_pozo_actual)

    print("\n", "Ingrese el valor que quieres apostar:")

    print("")

    monto_apostado = int(input("\t"))

    print("")

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

        carta_jugador_1 = analisis_AS(puntaje_actual_jugador, carta_jugador_1)

        puntaje_actual_jugador = carta_jugador_1

        carta_jugador_2 = analisis_AS(puntaje_actual_jugador, carta_jugador_2)

        puntaje_actual_jugador = carta_jugador_1 + carta_jugador_2

        carta_croupier_1 = analisis_AS(puntaje_actual_croupier, carta_croupier_1)

        puntaje_actual_croupier = carta_croupier_1

        analisis_BJN_jugador = carta_jugador_1 + carta_jugador_2

        analisis_BJN_crupier = carta_croupier_1 + carta_croupier_2

        time.sleep(1)

        print("\n", "Tu primera carta es: ", carta_jugador_1_tupla)

        time.sleep(1)

        print("\n", "Tu segunda carta es: ", carta_jugador_2_tupla)

        print("")

        print("º" * 100)

        print("º" * 100)

        time.sleep(1)

        print("\n", "la primera carta del croupier es: ", carta_croupier_1_tupla)

        print("")

        print("º" * 100)

        print("º" * 100)

        time.sleep(1)

        print("\n", "Tu puntaje actual es: ", puntaje_actual_jugador)

        time.sleep(1)

        print("\n","El puntaje actual del croupier: ", puntaje_actual_croupier)

        print("")

        print("º" * 100)

        print("º" * 100)

        while puntaje_actual_jugador < 21 and desicion_jugador == 1:

            time.sleep(1)

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

                carta_jugador = analisis_AS(puntaje_actual_jugador, carta_jugador)

                puntaje_actual_jugador += carta_jugador

                time.sleep(1)


                print("\n", "Tu nueva carta es:", carta_jugador_tupla)

                time.sleep(1)

                print("\n", "Tu puntaje actual es: ", puntaje_actual_jugador)

                print("")

                print("º" * 100)

                print("º" * 100)

                print("")

                while puntaje_actual_jugador >= 21 and puntaje_actual_croupier < 17:

                    nombre_carta_croupier, palo_carta_croupier, carta_croupier = generador_1()

                    carta_croupier_tupla = (nombre_carta_croupier, palo_carta_croupier)

                    time.sleep(1)

                    print("\nLa nueva carta del croupier es: ", carta_croupier_tupla)

                    carta_croupier = analisis_AS(puntaje_actual_croupier, carta_croupier)

                    puntaje_actual_croupier += carta_croupier

                    time.sleep(1)

                    print("\nPuntaje actual del croupier: ", puntaje_actual_croupier)

                    print("")

                    print("º" * 100)

                    print("º" * 100)

            elif decision_jugador == 2:

                puntaje_final_jugador = puntaje_actual_jugador

                time.sleep(1)

                print("\n", "Tu puntaje final es: ", puntaje_final_jugador)

                time.sleep(1)

                print("")

                print("La segunda carta del croupier es: ", carta_croupier_2_tupla)

                print("")

                print("º" * 100)

                print("º" * 100)

                carta_croupier_2 = analisis_AS(puntaje_actual_croupier, carta_croupier_2)

                puntaje_actual_croupier = carta_croupier_1 + carta_croupier_2

                while puntaje_actual_croupier < 17:

                    nombre_carta_croupier, palo_carta_croupier, carta_croupier = generador_1()

                    carta_croupier_tupla = (nombre_carta_croupier, palo_carta_croupier)

                    time.sleep(1)

                    print("\nLa nueva carta del croupier es: ", carta_croupier_tupla)

                    carta_croupier = analisis_AS(puntaje_actual_croupier, carta_croupier)

                    puntaje_actual_croupier += carta_croupier

                    time.sleep(1)

                    print("\nPuntaje actual del croupier: ", puntaje_actual_croupier)


                time.sleep(1)

                print("\n", "Verificando ganador de ronda")

                time.sleep(1)

                print("")

                print("º" * 100)

                print("º" * 100)

                validacion, monto_pozo_actual, contador_bj_natural = Resultado(puntaje_actual_jugador, puntaje_actual_croupier, monto_apostado, monto_pozo_actual, analisis_BJN_jugador, analisis_BJN_crupier)

                print("º" * 100)

                print("º" * 100)

                print("º" * 100)

                time.sleep(1)

                return monto_pozo_actual, validacion, monto_apostado, contador_bj_natural

            else:

                time.sleep(1)

                print("\n", "Lea bien las opciones, esocoja una valida, no sea menso")

                time.sleep(1.5)

        if puntaje_actual_jugador > 21:

            puntaje_final_jugador = puntaje_actual_jugador

            puntaje_final_croupier = puntaje_actual_croupier

            time.sleep(1)

            print("\n", "La mano ah finalizado, a continuacion sera redirigido al menu principal")

            time.sleep(1)

            print("\n", "Verificando ganador de ronda")

            time.sleep(1)

            print("")

            print("º" * 100)

            print("º" * 100)

            validacion, monto_pozo_actual, contador_bj_natural = Resultado(puntaje_actual_jugador, puntaje_actual_croupier, monto_apostado, monto_pozo_actual, analisis_BJN_jugador, analisis_BJN_crupier)

            print("º" * 100)

            print("º" * 100)

            print("º" * 100)

            time.sleep(1)

            return monto_pozo_actual, validacion, monto_apostado, contador_bj_natural

        if puntaje_actual_jugador == 21:

            puntaje_final_jugador = puntaje_actual_jugador

            puntaje_final_croupier = puntaje_actual_croupier

            time.sleep(1)

            print("\n", "La mano ah finalizado, a continuacion sera redirigido al menu principal")

            time.sleep(1)

            print("\n", "Verificando ganador de ronda")

            time.sleep(1)

            print("")

            print("º" * 100)

            print("º" * 100)

            validacion, monto_pozo_actual, contador_bj_natural = Resultado(puntaje_actual_jugador, puntaje_actual_croupier, monto_apostado, monto_pozo_actual, analisis_BJN_jugador, analisis_BJN_crupier)

            print("º" * 100)

            print("º" * 100)

            print("º" * 100)

            time.sleep(1)

            return monto_pozo_actual, validacion, monto_apostado, contador_bj_natural
