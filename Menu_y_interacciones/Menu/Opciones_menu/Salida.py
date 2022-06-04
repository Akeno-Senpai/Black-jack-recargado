def salir (Victorias_jugador, Partidas_jugadas, racha_crupier):

    racha_crupier_max = 0

    if racha_crupier > racha_crupier_max:

        racha_crupier_max = racha_crupier

    else:

        racha_crupier_max = racha_crupier

    Porcentaje_victorias = (Victorias_jugador * 100) // Partidas_jugadas

    print("Ganaste:", Victorias_jugador, " partidas")

    print("Se jugaron: ", Partidas_jugadas, " partidas")

    print("\n", 'El porcentaje de victorias del jugador es: ', Porcentaje_victorias)

    print("\n", "La racha de victorias mas grande del croupier es: ", racha_crupier_max)
