from typing import List, Tuple
from functools import reduce


def leer_mapa(nombre_archivo: str) -> Tuple[str, List[str]]:
    with open(nombre_archivo) as archivo:
        lineas = archivo.readlines()
    coordenadas = lineas.pop(0).strip().split()
    return reduce(lambda x, y: x + y, lineas).strip(), coordenadas


def convertir_a_matriz(laberinto: str) -> List[List[str]]:
    filas = laberinto.strip().split("\n")
    matriz = [list(fila) for fila in filas]
    return matriz


import os


def mostrar_matriz(matriz: List[List[str]]):
    os.system("cls" if os.name == "nt" else "clear")
    for fila in matriz:
        print("".join(fila))


def jugar_laberinto(
    matriz: List[List[str]], inicio: Tuple[int, int], final: Tuple[int, int]
):
    px, py = inicio
    while (px, py) != final:
        matriz[py][px] = "P"
        mostrar_matriz(matriz)
        tecla = input()
        if tecla == "\x1b[A":
            nueva_py = py - 1
            if nueva_py >= 0 and matriz[nueva_py][px] != "#":
                matriz[py][px] = "."
                py = nueva_py
                matriz[py][px] = "P"
        elif tecla == "\x1b[B":
            nueva_py = py + 1
            if nueva_py < len(matriz) and matriz[nueva_py][px] != "#":
                matriz[py][px] = "."
                py = nueva_py
                matriz[py][px] = "P"
        elif tecla == "\x1b[D":
            nueva_px = px - 1
            if nueva_px >= 0 and matriz[py][nueva_px] != "#":
                matriz[py][px] = "."
                px = nueva_px
                matriz[py][px] = "P"
        elif tecla == "\x1b[C":
            nueva_px = px + 1
            if nueva_px < len(matriz[0]) and matriz[py][nueva_px] != "#":
                matriz[py][px] = "."
                px = nueva_px
                matriz[py][px] = "P"
    matriz[py][px] = "F"
    mostrar_matriz(matriz)
    print("¡Felicidades! ¡Has ganado!")


# Llama a la función leer_mapa() para obtener el laberinto y las coordenadas.
laberinto, coordenadas = leer_mapa("mapa.txt")

# Convierte el laberinto de cadena a matriz.
matriz = convertir_a_matriz(laberinto)

# Define las coordenadas iniciales y finales del jugador.
inicio = (0, 0)
final = (int(coordenadas[1]) - 1, int(coordenadas[0]) - 1)

# Juega el laberinto.
jugar_laberinto(matriz, inicio, final)
