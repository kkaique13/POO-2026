from figura2d import Figura2D
from math import pi

class Circulo(Figura2D):
    def __init__(self, cor:str, raio:float) -> None:
        super().__init__(cor)
        self.raio = raio

    def calcularArea(self) -> float:
        return math.pi * (self.raio**2)
