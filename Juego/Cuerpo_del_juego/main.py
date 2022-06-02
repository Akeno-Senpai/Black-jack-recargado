

def black_jack():

    from Menu_y_interacciones.Inicio.bienvenida import datos_jugador

    from Menu_y_interacciones.Menu.menu_opciones import menu_opciones

    valor_pozo_incial, nombre_jugador, apellido_jugador = datos_jugador()

    menu_opciones(valor_pozo_incial)


