import abc #Abstract Base Classes
class Figura(abc.ABC):
    def __init__(self, cor:str) -> None:
        self.__cor = cor
    
    @property
    def cor(self) -> str:
        return self.__cor
    
    @cor.setter
    def cor(self, cor:str) -> None:
        self.__cor = cor
    
    @abc.abstractmethod
    def calcularArea(self) -> str:
        pass
    
    @abc.abstractmethod
    def retornarDados(self) -> str:
        pass