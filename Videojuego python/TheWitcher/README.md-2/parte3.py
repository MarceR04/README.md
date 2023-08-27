# Importar los módulos necesarios
import os
import keyboard

# Definir la función que borra la terminal e imprime el nuevo número
def borrar_e_imprimir(numero):
    # Borrar la terminal según el sistema operativo
    os.system('cls' if os.name=='nt' else 'clear')
    # Imprimir el número
    print(numero)

# Iniciar con un número en 0
numero = 0

# Leer la tecla n del teclado en un bucle
while True:
    # Si la tecla n está presionada
    if keyboard.is_pressed('n'):
        # Incrementar el número en 1
        numero += 1
        # Llamar a la función que borra la terminal e imprime el nuevo número
        borrar_e_imprimir(numero)
        # Si el número llega a 50, salir del bucle
        if numero == 50:
            break

