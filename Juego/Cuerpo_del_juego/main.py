

def black_jack():

    racha_crupier = 0

    from Menu_y_interacciones.Inicio.bienvenida import datos_jugador

    from Menu_y_interacciones.Menu.menu_opciones import menu_opciones

    valor_pozo_incial, nombre_jugador, apellido_jugador = datos_jugador()

    racha_crupier = menu_opciones(valor_pozo_incial, racha_crupier)




