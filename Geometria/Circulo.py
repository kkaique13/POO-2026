from Figura import Figura
from math import pi
class Circulo(Figura):
    def __init__(self, cor:str, raio:float) -> None:
        super().__init__(cor)
        self.__raio = raio
    
    @property
    def raio(self) -> float:
        return self.__raio
    
    @raio.setter
    def raio(self, raio:float) -> None:
        self.__raio = raio
    
    def calcularArea(self) -> str:
        return f"{pi * (self.__raio ** 2):.2f} m²"
    
    def retornarDados(self) -> str:
        return f"Círculo {self.cor} com raio {self.__raio}\nÁrea: {self.calcularArea()}\n"