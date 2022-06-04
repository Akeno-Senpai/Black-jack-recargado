

def Contadores(racha_crupier, Victorias_jugador, Partidas_jugadas, validacion):

    if validacion == 0 or validacion == 1 or validacion == 2:

                Partidas_jugadas += 1

                if validacion == 1:

                    racha_crupier += 1

                elif validacion == 0:

                    Victorias_jugador += 1
    validacion = 0

    return racha_crupier, Victorias_jugador, Partidas_jugadas, validacion
