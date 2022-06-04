def salir (Victorias_jugador, Partidas_jugadas, racha_crupier, monto_actual, apuesta_actual, validacion, total_apuestas, monto_pozo_incial, apuesta_inicial):

    from Menu_y_interacciones.Menu.Opciones_menu.Estadisticas import estadisticas

    racha_crupier_max = 0

    if racha_crupier > racha_crupier_max:

        racha_crupier_max = racha_crupier

    else:

        racha_crupier_max = racha_crupier

    Porcentaje_victorias = (Victorias_jugador * 100) // Partidas_jugadas

    monto_maximo, promedio_apuestas, apuesta_max_perdida, total_apuestas = estadisticas(monto_actual, apuesta_actual, Partidas_jugadas, validacion, total_apuestas, monto_pozo_incial, apuesta_inicial)


    print("Ganaste:", Victorias_jugador, " partidas")

    print("Se jugaron: ", Partidas_jugadas, " partidas")

    print("\n", 'El porcentaje de victorias del jugador es: ', Porcentaje_victorias)

    print("\n", "La racha de victorias mas grande del croupier es: ", racha_crupier_max)

    return total_apuestas
