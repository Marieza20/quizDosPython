class Juego:
    def __init__(self, nombreJ):
        self.nombreJ = nombreJ
        self.jugando = False
    
    def iniciar(self):
        self.jugando = True
        print(f"Bienvenido(a) {self.nombreJ}, el juego ha comenzado.")
        
        print("¡Gracias por jugar!")
        
    def salir(self):
        print("Saliendo del juego...")