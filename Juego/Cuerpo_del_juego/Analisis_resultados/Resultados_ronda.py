

def Resultado(Puntaje_Total_jugador,Puntaje_Total_Croupier,monto_apostado,monto_pozo_actual):
    if (Puntaje_Total_jugador <= 21) and (Puntaje_Total_Croupier < Puntaje_Total_jugador) or (Puntaje_Total_jugador <= 21 and Puntaje_Total_Croupier > 21):
        validacion = 0

        print ('\nHas ganado esta ronda', '\nTu puntaje es: ', Puntaje_Total_jugador,'\ny el del Croupier es: ',Puntaje_Total_Croupier)

    elif (Puntaje_Total_Croupier > Puntaje_Total_jugador) and (Puntaje_Total_Croupier <= 21) or (Puntaje_Total_jugador > 21):
        validacion = 1

        print ('\nHas perdido esta ronda', '\nTu puntaje es: ',Puntaje_Total_jugador,'\ny el del Croupier es: ',Puntaje_Total_Croupier)

    elif (Puntaje_Total_jugador == Puntaje_Total_Croupier) or (Puntaje_Total_jugador and Puntaje_Total_Croupier == 21):
        validacion = 2

        print ('\nHa ocurrido un empate', '\nTu puntaje es: ',Puntaje_Total_jugador,'\ny el del Croupier es: ',Puntaje_Total_Croupier)

    if validacion == 0:
        monto_pozo_actual += monto_apostado * 2
        print ("Tras la apuesta, tu monto actuaes es igual a:", monto_pozo_actual)

    elif validacion == 1
        monto_pozo_actual -= monto_apostado
        print("Tras la apuesta, tu monto actuaes es igual a:", monto_pozo_actual)

    elif validacion == 2
        monto_pozo_actual = monto_pozo_actual
        print("Tras la apuesta, tu monto actuaes es igual a:", monto_pozo_actual)


    return validacion, monto_pozo_actual


