def estadisticas(monto_actual, apuesta_actual, cantidad_apuestas, validacion, apuesta_max_perdidav2, total_apuestas):

    monto_maximo = 0
    apuesta_max_perdida = apuesta_max_perdidav2
    total_apuestas += apuesta_actual
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

    print(monto_maximo, "Monto_maximo")
    print(promedio_apuestas, "Promedio apuestas")
    print(total_apuestas, "Total apuestas")
    print(apuesta_max_perdida, "Apuestas perdidas")


    return monto_maximo, promedio_apuestas, apuesta_max_perdida
