from typing import List, Tuple

def convertir_a_matriz(laberinto: str) -> List[List[str]]:
    # Separa la cadena en filas.
    filas = laberinto.strip().split("\n")

    # Convierte cada fila en una lista de caracteres.
    matriz = [list(fila) for fila in filas]

    return matriz

import os

def mostrar_matriz(matriz: List[List[str]]):
    # Limpia la pantalla.
    os.system("cls" if os.name == "nt" else "clear")

    # Muestra cada fila de la matriz.
    for fila in matriz:
        print("".join(fila))

def jugar_laberinto(matriz: List[List[str]], inicio: Tuple[int, int], final: Tuple[int, int]):
    # Define las coordenadas iniciales del jugador.
    px, py = inicio

    # Mientras el jugador no llegue al final.
    while (px, py) != final:
        # Asigna el caracter P a las coordenadas del jugador.
        matriz[py][px] = "P"

        # Muestra la matriz en la pantalla.
        mostrar_matriz(matriz)

        # Lee la tecla presionada por el usuario.
        tecla = input()

        # Verifica si la tecla es una flecha hacia arriba.
        if tecla == "\x1b[A":
            nueva_py = py - 1
            if nueva_py >= 0 and matriz[nueva_py][px] != "#":
                matriz[py][px] = "."
                py = nueva_py
                matriz[py][px] = "P"

        # Verifica si la tecla es una flecha hacia abajo.
        elif tecla == "\x1b[B":
            nueva_py = py + 1
            if nueva_py < len(matriz) and matriz[nueva_py][px] != "#":
                matriz[py][px] = "."
                py = nueva_py
                matriz[py][px] = "P"

        # Verifica si la tecla es una flecha hacia la izquierda.
        elif tecla == "\x1b[D":
            nueva_px = px - 1
            if nueva_px >= 0 and matriz[py][nueva_px] != "#":
                matriz[py][px] = "."
                px = nueva_px
                matriz[py][px] = "P"

        # Verifica si la tecla es una flecha hacia la derecha.
        elif tecla == "\x1b[C":
            nueva_px = px + 1
            if nueva_px < len(matriz[0]) and matriz[py][nueva_px] != "#":
                matriz[py][px] = "."
                px = nueva_px
                matriz[py][px] = "P"


laberinto = "###.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.#.###\n#...#...#...#...#...#...#...#...#...#\n#.###.#.###.###.#.###.###.#.###.###.#\n#.#...#...#...#...#...#...#.#.....#.#\n#.###.###.#.#####.###.###.#.#####.#.#\n#...#.....#.....#.....#...#.......#.#\n###.#.#########.#####.###.##########"
inicio = (0, 0)
final = (29, 6)
jugar_laberinto(convertir_a_matriz(laberinto), inicio, final)
