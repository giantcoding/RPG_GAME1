class Vista:
    @staticmethod
    def mostrar_bienvenida():
        print("¡Bienvenido al juego 'La Senda del Destino'!")

    @staticmethod
    def obtener_nombre_jugador():
        return input("Por favor, ingresa tu nombre: ")

    @staticmethod
    def elegir_clase():
        print("Elige una clase:")
        print("1. Orco")
        print("2. Arquero")
        print("3. Guerrero")
        return input("Ingresa el número de la clase que deseas: ")

    @staticmethod
    def mostrar_historia_y_info(historia, info_clase):
        print(historia)
        print(info_clase)

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)

