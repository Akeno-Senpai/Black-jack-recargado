

def Contadores(Victorias_jugador, Partidas_jugadas, validacion, apuesta_actual, racha_croupier, racha_croupier_max):

    if validacion == 0 or validacion == 1 or validacion == 2:

        Partidas_jugadas += 1

        if validacion == 1:

            racha_croupier_max += racha_croupier

        elif validacion == 0:

            racha_croupier = 0

            Victorias_jugador += 1

        if Partidas_jugadas == 1:

            apuesta_inicial = apuesta_actual

    validacion = -1

    return Victorias_jugador, Partidas_jugadas, validacion, racha_croupier_max


