from Figura import Figura
class Quadrado(Figura):
    def __init__(self, cor:str, lado:float) -> None:
        super().__init__(cor)
        self.__lado = lado
    
    @property
    def lado(self) -> float:
            return self.__lado
    
    @lado.setter
    def lado(self, lado:float) -> None:
            self.__lado = lado
    
    def calcularArea(self) -> str:
        return f"{(self.__lado ** 2):.2f} m²"
    
    def retornarDados(self) -> str:
        return f"Quadrado {self.cor} com lado {self.__lado}\nÁrea: {self.calcularArea()}\n"