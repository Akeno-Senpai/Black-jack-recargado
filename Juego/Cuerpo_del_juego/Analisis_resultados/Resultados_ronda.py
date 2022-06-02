

def Resultado(Puntaje_Total_jugador,Puntaje_Total_Croupier):
    if (Puntaje_Total_jugador <= 21) and (Puntaje_Total_Croupier < Puntaje_Total_jugador) or (Puntaje_Total_jugador <= 21 and Puntaje_Total_Croupier > 21):


        print ('\nHas ganado esta ronda', '\nTu puntaje es: ', Puntaje_Total_jugador,'\ny el del Croupier es: ',Puntaje_Total_Croupier)

    elif (Puntaje_Total_Croupier > Puntaje_Total_jugador) and (Puntaje_Total_Croupier <= 21) or (Puntaje_Total_jugador > 21):


        print ('\nHas perdido esta ronda', '\nTu puntaje es: ',Puntaje_Total_jugador,'\ny el del Croupier es: ',Puntaje_Total_Croupier)

    elif (Puntaje_Total_jugador == Puntaje_Total_Croupier) or (Puntaje_Total_jugador and Puntaje_Total_Croupier == 21):


        print ('\nHa ocurrido un empate', '\nTu puntaje es: ',Puntaje_Total_jugador,'\ny el del Croupier es: ',Puntaje_Total_Croupier)

