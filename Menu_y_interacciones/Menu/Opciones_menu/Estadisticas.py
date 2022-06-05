

def estadisticas(monto_actual, apuesta_actual, cantidad_apuestas, validacion, total_apuestas, monto_pozo_inicial, apuesta_inicial):
    monto_maximo = monto_pozo_inicial
    apuesta_max_perdida = apuesta_inicial
    print(cantidad_apuestas, "cantidad de apuestas")
    print(apuesta_actual, "La apuesta actual")

    #El monto máximo que llegó a tener el jugador en el pozo.

    if monto_maximo < monto_actual:

        monto_maximo = monto_actual

    #El monto promedio del que dispuso el jugador para realizar apuestas.

    promedio_apuestas = total_apuestas / cantidad_apuestas

    #La pérdida más grande que sufrió el jugador (si hubo alguna)

    if apuesta_max_perdida < apuesta_actual and validacion == 1:

        apuesta_max_perdida = apuesta_actual

    return monto_maximo, promedio_apuestas, apuesta_max_perdida
