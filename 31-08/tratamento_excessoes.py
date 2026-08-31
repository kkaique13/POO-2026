class ContaBancaria:
    def __init__(self, titular:str, saldo:float) -> None:
        self.titular = titular
        self.__saldo = saldo
    @property
    def saldo(self) -> float:
        return self.__saldo

    def saque(self, valor:float) -> None:
        if valor > 0:
            self.__saldo -= valor

valores = [200.00, 350.00, 47.50]
nome = input("Informe o nome do(a) titular: \n")
inicial = float(input("Qual o saldo inicial? \n"))
conta = ContaBancaria(nome, inicial)

for valor in valores:
    try:
        conta.saque(valor)
    except ValueError:
        print(f"Valor R${valor} inválido para o saque! ")
    except:
        print("Ocorreu um erro no sistema. ")
    else:
        print(f"Saque de R${valor} realizado com sucesso! ")
    finally:
        print("Conexões finalizadas. ")