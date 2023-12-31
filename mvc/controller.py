from mvc.view import Vista
from mvc.model import Arquero, Orco, Guerrero

class Controlador:
    def __init__(self):
        self.vista = Vista()

    def iniciar_juego(self):
        self.vista.mostrar_bienvenida()
        nombre_jugador = self.vista.obtener_nombre_jugador()
        
        while True:
            opcion_clase = self.vista.elegir_clase()
            
            if opcion_clase == "1":
                clase_elegida = Orco(nombre_jugador)
                break
            elif opcion_clase == "2":
                clase_elegida = Arquero(nombre_jugador)
                break
            elif opcion_clase == "3":
                clase_elegida = Guerrero(nombre_jugador)
                break
            else:
                self.vista.mostrar_mensaje("Opción no válida. Por favor, elige 1, 2 o 3.")
        
        historia, info_clase = self.obtener_historia_y_info(clase_elegida)
        self.vista.mostrar_historia_y_info(historia, info_clase)
        self.vista.mostrar_mensaje(f"Has elegido la clase {clase_elegida.nombre}. ¡Buena suerte!")


    def obtener_historia_y_info(self, clase_elegida):
        if isinstance(clase_elegida, Orco):
            historia = Vista.obtener_historia_orco()
        elif isinstance(clase_elegida, Arquero):
            historia = Vista.obtener_historia_arquero()
        elif isinstance(clase_elegida, Guerrero):
            historia = Vista.obtener_historia_guerrero()
        
        info_clase = f"Vida: {clase_elegida.vida}, Daño: {clase_elegida.daño}"
        return historia, info_clase