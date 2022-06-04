def Contadores(Victorias_jugador, Partidas_jugadas, validacion, monto_apostado):

    monto_apostado_total = 0

    racha_crupier = 0

    if validacion == 0 or validacion == 1 or validacion == 2:

        Partidas_jugadas += 1

        if validacion == 1:

            racha_crupier += 1

        elif validacion == 0:

            Victorias_jugador += 1

        monto_apostado_total += monto_apostado

    validacion = 0

    return Victorias_jugador, Partidas_jugadas, validacion, monto_apostado_total, racha_crupier

