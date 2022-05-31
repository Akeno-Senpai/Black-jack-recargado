#Solicitar datos del jugador tales como: Nombre, Apellido y monto del pozo#

def datos_jugador():



    #Variables#


    from Menu_y_interacciones.Inicio.Analisis_pozo import pozo_menor_100000
    nombre_jugador = ""
    apellido_jugador = ""
    monto_inical_pozo = 0
    bandera = True
    inicio = 0


    #Variables#


    print("")
    print("*" * 40)
    print("\n Black Jack: Recargado \n")
    print("*" * 40)
    print("")
    print("")
    print("Importante, leer antes de continuar: \n")
    print("\t* El monto del pozo no puede ser mayor a 100000$")
    print("\t* El monto del pozo no puede ser menor a 1$")


    inicio = int(input("\nSi aun asi usted desea continuar, presione uno:\t "))
    nombre_jugador = ""
    apellido_jugador = ""
    monto_inical_pozo = 0
    bandera = True
    while bandera:
        if inicio == 1:
            nombre_jugador = input("Ingrese su nombre para poder continuar: ")
            apellido_jugador = input("Ingrese su apellido para poder continuar: ")
            monto_inical_pozo_validacion, monto_inical_pozo = pozo_menor_100000()
            while monto_inical_pozo_validacion == False:
                     monto_inical_pozo_validacion, monto_inical_pozo = pozo_menor_100000()
            print(" ")
            print("*" * 40)
            print("\nSea cordialmente bienvendio a Black Jack: Recargado señor: ", nombre_jugador, apellido_jugador)
            print("Usted cuenta con un monto de: ", monto_inical_pozo, "$", " dentro de su pozo \n")
            print("*" * 40)
            bandera = False
        else:
            salir = int(input(
                "Si desea salir del programa precione uno, si aun quiere continuar precione dos:\t "))
            if salir == 1:
                print("El programa se cerrara \n")
                bandera = False
            else:
                bandera = True

    return monto_inical_pozo, nombre_jugador, apellido_jugador

datos_jugador()
