

def apostar(monto_inicial_jugador):

    #print("Tienes el siguiente monto en tu pozo:",monto_inicial_jugador)
    nueva_apuesta = int(input('Ingrese la cantidad que quiere agregar a su pozo. Mayor a 1 y menor a 100000: '))
    pozo_jugador = monto_inicial_jugador
    Monto_inicial_jugador = monto_inicial_jugador


    bandera = True

    while bandera == True:
        if nueva_apuesta > 1 and nueva_apuesta <100000:
            suma_apuesta = pozo_jugador + nueva_apuesta

            pozo_jugador = suma_apuesta
            bandera = False
            print('El monto se ah actualizado correctmente.')
        else:
            nueva_apuesta = int(input("Ingrese un valor valido para agregar a su pozo: "))
            bandera = True


    return pozo_jugador, Monto_inicial_jugador
