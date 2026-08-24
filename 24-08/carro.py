class Veiculo:
    def __init__(self, placa:str, cor:str) -> None:
        self.placa = placa
        self.cor = cor

class Carro(Veiculo):
    def __init__(self, placa:str, cor:str, nome:str, preco:float) -> None:
        super().__init__(placa, cor)
        self.nomeFornecedor = nome
        self.preco = preco
        
    def getNoneFornecedor(self) -> str:
        return self.nomeFornecedor
    
    def getPreco(self) -> float:
        return self.preco
    
    def setPreco(self, preco:float) -> None:
        if preco > self.preco:
            self.preco = preco