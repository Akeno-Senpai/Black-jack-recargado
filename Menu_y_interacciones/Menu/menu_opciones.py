

def menu_opciones(valor_pozo_inicial, racha_crupier):

    from Menu_y_interacciones.Menu.Opciones_menu.Apostar import apostar

    from Menu_y_interacciones.Menu.Opciones_menu.Jugar_una_mano import jugar_una_mano

    from Menu_y_interacciones.Menu.Opciones_menu.Salida import salir

    import time

    opcion = -1

    #valor_apostar = 0

    monto_pozo_actual = valor_pozo_inicial

    while opcion != 0:

        print("Menu de opciones")

        print("\n1- Apostar")

        print("\n2- Jugar una mano")

        print("\n3- Salir")

        opcion = int(input("\nIngrese la opcion que quiere realizar: "))

        if opcion == 1:
            print("Tienes en tu pozo :",monto_pozo_actual )
            monto_pozo_actual, monto_inicial_pozo = apostar(monto_pozo_actual)



        elif opcion == 2:

            jugar_una_mano(monto_pozo_actual, valor_pozo_inicial)

        elif opcion == 3:
            Victorias_jugador, Partidas_jugadas = 0
            salir(Victorias_jugador, Partidas_jugadas, racha_crupier)

        else:

            print("\nLea bien las opciones del menu. [Valor ingresado no valido]")

            time.sleep(1.5)

            print("Precione enter para volver al menu: ")

            input()
    return racha_crupier
