import random

# CLASE PERSONAJES

class Personaje:
    def __init__(self, nombre, vida, daño):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño

    def atacar(self, objetivo):
        # Método para realizar un ataque
        objetivo.recibir_daño(self.daño)

    def recibir_daño(self, cantidad):
        # Método para recibir daño
        self.vida -= cantidad

    def esta_vivo(self):
        # Método para comprobar si el personaje está vivo
        return self.vida > 0

    def __str__(self):
        return f"{self.nombre} (Vida: {self.vida}, Daño: {self.daño}"

class Arquero(Personaje):
    def __init__(self, nombre):
        vida = random.randint(60, 100)
        daño = random.randint(8, 10)
        super().__init__(nombre, vida, daño)

class Orco(Personaje):
    def __init__(self, nombre):
        vida = random.randint(90, 120)
        daño = random.randint(6, 7)
        super().__init__(nombre, vida, daño)

class Guerrero(Personaje):
    def __init__(self, nombre):
        vida = random.randint(75, 105)
        daño = random.randint(7, 9)
        super().__init__(nombre, vida, daño)

# CLASE OBJETO

class Objeto:
    def __init__(self, nombre):
        self.nombre = nombre

    def usar(self, personaje):
        pass

class Pocion(Objeto):
    def __init__(self):
        super().__init__("Poción")

    def usar(self, personaje):
        # Lógica para usar la poción y restaurar la vida del personaje
        personaje.vida += 25

class Veneno(Objeto):
    def __init__(self):
        super().__init__("Veneno")

    def usar(self, personaje):
        # Lógica para usar el veneno y quitar puntos de vida al personaje
        personaje.vida -= 10