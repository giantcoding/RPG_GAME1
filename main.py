from mvc.controller import Controlador

def main():
    juego = Controlador()
    try:
        juego.iniciar_juego()
    except Exception as e:
        print(f"Se produjo un error en el juego: {e}")

if __name__ == "__main__":
    main()