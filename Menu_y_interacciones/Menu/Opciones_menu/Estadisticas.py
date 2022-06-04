def estadisticas(monto_actual, apuesta_actual, cantidad_apuestas, validacion, apuesta_max_perdidav2):

    monto_maximo = 0
    apuesta_max_perdida = apuesta_max_perdidav2
    total_apuestas = 0
    total_apuestas += apuesta_actual

    #El monto máximo que llegó a tener el jugador en el pozo.

    if monto_maximo < monto_actual:

        monto_maximo = monto_actual

    #El monto promedio del que dispuso el jugador para realizar apuestas.

    promedio_apuestas = total_apuestas / cantidad_apuestas

    #La pérdida más grande que sufrió el jugador (si hubo alguna)

    if apuesta_max_perdida < apuesta_actual and validacion == 1:

        apuesta_max_perdida = apuesta_actual



    return monto_maximo, promedio_apuestas, apuesta_max_perdida
