from abc import *

class Figura2D(ABC):
    def __init__(self, cor:str) -> None:
        self.cor = cor
    
    @abstractmethod
    def calcularArea(self) -> float:
        pass

