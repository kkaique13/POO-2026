from figura2d import Figura2D

class Retangulo(Figura2D):
    def __init__(self, cor:str, base:float, altura:float) -> None:
        super().__init__(cor)
        self.base = base
        self.altura = altura

    def calcularArea(self) -> float:
        return self.base * self.altura

    def inclinar(self, eixo:str) -> None:
        pass