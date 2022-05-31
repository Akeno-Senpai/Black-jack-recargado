from Menu_y_interacciones.Inicio.Analisis_pozo import pozo_menor_100000
from Menu_y_interacciones.Inicio.bienvenida import datos_jugador

def apostar():

    validación, apostar_ = pozo_menor_100000()
    monto_inical_pozo  = datos_jugador()
    print(monto_inical_pozo)
    while validación == False:
        pass
apostar()
