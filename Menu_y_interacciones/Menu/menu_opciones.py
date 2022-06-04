

def menu_opciones(valor_pozo_inicial):

    from Menu_y_interacciones.Menu.Opciones_menu.Apostar import apostar

    from Menu_y_interacciones.Menu.Opciones_menu.Jugar_una_mano import jugar_una_mano

    from Menu_y_interacciones.Menu.Opciones_menu.Salida import salir

    from Menu_y_interacciones.Menu.Opciones_menu.Contadores import Contadores

    import time

    opcion = -1

    validacion = 0

    racha_crupier = 0

    #valor_apostar = 0

    monto_pozo_actual = valor_pozo_inicial

    acha_crupier, Victorias_jugador, Partidas_jugadas = 0, 0, 0

    partidas_jugadas = 0


    while opcion != 0:

        print("\nMenu de opciones")

        print("\n1- Apostar")

        print("\n2- Jugar una mano")

        print("\n3- Salir")

        opcion = int(input("\nIngrese la opcion que quiere realizar: "))



        if opcion == 1:

            print("Tienes en tu pozo :",monto_pozo_actual )

            monto_pozo_actual, monto_inicial_pozo = apostar(monto_pozo_actual)

        elif opcion == 2:

            monto_pozo_actual, validacion, racha_crupier = jugar_una_mano(monto_pozo_actual, valor_pozo_inicial)
        elif opcion == 3:

            salir(Victorias_jugador, Partidas_jugadas, racha_crupier)

        else:

            print("\nLea bien las opciones del menu. [Valor ingresado no valido]")

            time.sleep(1.5)

            print("Precione enter para volver al menu: ")

            input()


        racha_crupier, Victorias_jugador, Partidas_jugadas, validacion = Contadores(racha_crupier, Victorias_jugador, Partidas_jugadas, validacion)
