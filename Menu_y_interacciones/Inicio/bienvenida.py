#Solicitar datos del jugador tales como: Nombre, Apellido y monto del pozo#


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


def datos_jugador():
    inicio = int(input("\nSi aun asi usted desea continuar, presione uno:\t "))
    nombre_jugador = ""
    apellido_jugador = ""
    monto_inical_pozo = 0
    bandera = True
    while bandera:
        if inicio == 1:
            nombre_jugador = input("Ingrese su nombre para poder continuar: ")
            apellido_jugador = input("Ingrese su apellido para poder continuar: ")
            monto_inical_pozo = int(
                input("Ingrese el monto desdeado para inciar el juego:\t "))
            monto_inical_pozo_validacion = pozo_menor_100000(monto_inical_pozo)
            while monto_inical_pozo_validacion:
                if monto_inical_pozo_validacion == True:
                    monto_inical_pozo = int(input("Ingrese un monto adecuado para inciar el juego:\t "))
                else:
                    monto_inical_pozo_validacion = False
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
