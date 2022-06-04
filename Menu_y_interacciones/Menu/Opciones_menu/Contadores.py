def Contadores(racha_crupier, Victorias_jugador, Partidas_jugadas, validacion, monto_apostado):

    contador_apuestas = 0
    monto_apostado_total = 0

    if validacion == 0 or validacion == 1 or validacion == 2:

        Partidas_jugadas += 1

        if validacion == 1:

            racha_crupier += 1

        elif validacion == 0:

            Victorias_jugador += 1

        if monto_apostado != 0:

            contador_apuestas += 1

        monto_apostado_total += monto_apostado

    validacion = 0

    return racha_crupier, Victorias_jugador, Partidas_jugadas, validacion, monto_apostado_total, contador_apuestas
