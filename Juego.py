class Juego:
    def __init__(self, nombreJ):
        self.nombreJ = nombreJ
        self.jugando = False
        self.abecedario = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    
    def iniciar(self):
        self.jugando = True
        print(f"Bienvenido(a) {self.nombreJ}, el juego ha comenzado.")
        Juego.desplazar(self)
        print("¡Gracias por jugar!")
        
    def iniciarDos(self):
        self.jugando = True
        print(f"Bienvenido(a) {self.nombreJ}, el juego ha comenzado.")
        Juego.desplazarDos(self)
        print("¡Gracias por jugar!")
        
    def iniciarTres(self):
        self.jugando = True
        print(f"Bienvenido(a) {self.nombreJ}, el juego ha comenzado.")
        Juego.desplazarTres(self)
        print("¡Gracias por jugar!")
        
    def salir(self):
        print("Saliendo del juego...")
        
    def desplazar(self):
        letras = input("Ingrese la palabra a encriptar: ")
        for letra in letras:
            letraMayuscula = letra.upper()
            if letraMayuscula in self.abecedario:
                posicion = self.abecedario.index(letraMayuscula)
                nuevaPosicion = posicion + 1
                if nuevaPosicion >= len(self.abecedario):
                    nuevaPosicion = 0
                letraEncriptada = self.abecedario[nuevaPosicion]
                print(letraEncriptada, end="")
        print("")
        
    def desplazarDos(self):
        desplazamiento = input("Ingrese el numero de desplazamiento para encriptar: ")
        letras = input("Ingrese la palabra a encriptar: ")
        for letra in letras:
            letraMayuscula = letra.upper()
            if letraMayuscula in self.abecedario:
                posicion = self.abecedario.index(letraMayuscula)
                nuevaPosicion = posicion + int(desplazamiento)
                if nuevaPosicion >= len(self.abecedario):
                    nuevaPosicion = nuevaPosicion - len(self.abecedario)
                letraEncriptada = self.abecedario[nuevaPosicion]
                print(letraEncriptada, end="")
        print("")
        
    def desplazarTres(self):
        desplazamiento = input("Ingrese el numero de desplazamiento para desencriptar: ")
        letras = input("Ingrese la palabra para desencriptar: ")
        for letra in letras:
            letraMayuscula = letra.upper()
            if letraMayuscula in self.abecedario:
                posicion = self.abecedario.index(letraMayuscula)
                nuevaPosicion = posicion - int(desplazamiento)
                if nuevaPosicion >= len(self.abecedario):
                    nuevaPosicion = 0
                letraEncriptada = self.abecedario[nuevaPosicion]
                print(letraEncriptada, end="")
        print("")