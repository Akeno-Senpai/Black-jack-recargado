

def menu_opciones(valor_pozo_inicial, bandera):

    from Menu_y_interacciones.Menu.Opciones_menu.Apostar import apostar

    from Menu_y_interacciones.Menu.Opciones_menu.Jugar_una_mano import jugar_una_mano

    from Menu_y_interacciones.Menu.Opciones_menu.Salida import salir

    from Menu_y_interacciones.Menu.Opciones_menu.Contadores import Contadores

    import time

    opcion = -1

    total_apuestas = 0

    validacion, racha_croupier, monto_apostado = 0, 0, 0

    monto_pozo_actual = valor_pozo_inicial

    Partidas_jugadas = 0

    Victorias_jugador = 0

    if bandera == True or valor_pozo_inicial != 0:

        while opcion != 0:

            validacion = -1

            print("\nMenu de opciones")

            print("\n1- Apostar")

            print("\n2- Jugar una mano")

            print("\n3- Salir")

            opcion = int(input("\nIngrese la opcion que quiere realizar: "))



            if opcion == 1:

                print("Tienes en tu pozo :",monto_pozo_actual )

                monto_pozo_actual, monto_inicial_pozo = apostar(monto_pozo_actual)

            elif opcion == 2:

               monto_pozo_actual, validacion, monto_apostado, contador_bj_natural = jugar_una_mano(monto_pozo_actual, valor_pozo_inicial)

            elif opcion == 3:

                 total_apuestas = salir(Victorias_jugador, Partidas_jugadas, racha_crupier, monto_pozo_actual, monto_apostado, validacion, total_apuestas, valor_pozo_inicial, apuesta_inicial)

            else:

                print("\nLea bien las opciones del menu. [Valor ingresado no valido]")

                time.sleep(1.5)

                print("Precione enter para volver al menu: ")

                input()


            Victorias_jugador, Partidas_jugadas, validacion, racha_crupier, apuesta_inicial = Contadores(Victorias_jugador, Partidas_jugadas, validacion, monto_apostado)

