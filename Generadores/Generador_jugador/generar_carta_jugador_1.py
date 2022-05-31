def generar_carta_jugador():
    import random

    nombres = ("AS", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K")
    valores = (11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)
    #indice = (0,  1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12)
    palos = ("Diamante", "Corazon", "Pica", "Trebol")

    ind_carta = random.randint (0,12)
    ind_palos = random. randint (0,3)
    nom_carta = nombres[ind_carta]
    val_carta = valores[ind_carta]
    palos_carta = palos[ind_palos]


    #primera_carta = val_carta , nom_carta, palos_carta
    #val_primera_carta = primera_carta[0]
    #nom_primera_carta = primera_carta[1]
    return nom_carta, palos_carta, val_carta


print(generar_carta_jugador())


