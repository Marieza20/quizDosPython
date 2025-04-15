from Juego import Juego

def mostrar_menu():
    print("Menú Principal")
    print("1. Iniciar Encriptar")
    print("2. Iniciar Encriptar manualmente")
    print("3. Iniciar Desencriptar")
    print("4. Salir")

def main():
    nombre = input("Ingresa tu nombre para continuar: ")
    juego = Juego(nombre)
    valor = True
    while valor:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            juego.iniciar()
        elif opcion == "2":
            juego.iniciarDos()
        elif opcion == "3":
            juego.iniciarTres()
        elif opcion == "4":
            juego.salir()
            valor = False
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

main()