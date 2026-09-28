from figura2d import Figura2D
from retangulo import Retangulo

class Quadrado(Figura2D):
    def __init__(self, cor:str, lado:float) -> None:
        super().__init__(cor)
        self.lado = lado

    def calcularArea(self) -> float:
        return self.lado**2

    def inclinar(self, eixo:str) -> None:
        pass