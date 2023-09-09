class Juego:
    def __init__(self, mapa, inicio, fin):
        self.mapa = mapa
        self.inicio = inicio
        self.fin = fin

    def mover(self, direccion):
        # Implementa la lógica para mover al jugador en una dirección dada
        pass

    def jugar(self):
        # Implementa la lógica principal del juego
        pass

    import os
import random

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        self.path_a_mapas = path_a_mapas
        self.mapa = self.leer_mapa()

    def leer_mapa(self):
        archivos = os.listdir(self.path_a_mapas)
        nombre_archivo = random.choice(archivos)
        path_completo = f"{self.path_a_mapas}/{nombre_archivo}"
        with open(path_completo, "r") as archivo:
            lineas = archivo.readlines()
            inicio_x, inicio_y, fin_x, fin_y, *filas = lineas
            mapa = "".join(filas).strip()
            return Mapa(mapa, (int(inicio_x), int(inicio_y)), (int(fin_x), int(fin_y)))



