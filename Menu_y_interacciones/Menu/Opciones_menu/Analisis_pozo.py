def pozo_menor_100000():
    a = int(input("Ingrese el monto desdeado para inciar el juego:\t "))
    if 1 < a < 100000:
        cancelar = True
        pozo = a

    else:
        cancelar = False
        pozo = a

    return cancelar, pozo
