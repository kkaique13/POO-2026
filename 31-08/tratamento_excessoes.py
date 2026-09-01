class SaldoInsuficiente(Exception):
    def __init__(self) -> None:
        super().__init__("Saldo Insuficiente!")

class ContaBancaria:
    def __init__(self, titular:str, saldo:float) -> None:
        self.titular = titular
        self.__saldo = saldo
    @property
    def saldo(self) -> float:
        return self.__saldo

    def saque(self, valor:float) -> None:
        if valor > 0:
            if valor > self.saldo:
                raise SaldoInsuficiente()
            self.__saldo -= valor

valores = []
nome = input("Informe o nome do(a) titular: \n")
inicial = float(input("Qual o saldo inicial? \n"))
conta = ContaBancaria(nome, inicial)

es = input("Deseja inserir um valor na sua lista de saques? (s/n) \n")

while es != 's' and es != 'n':
    print("Opção inválida! \n")
    es = input("Deseja inserir um valor na sua lista de saques? (s/n) \n")

while es == 's':
    try:
        valor = float(input("Insira o valor: "))
        if valor <= 0:
            raise ValueError()
        valores.append(valor)
        es = input("Deseja inserir um valor na sua lista de saques? (s/n) \n")
    except ValueError:
        print("Valor inválido!")
    if es == 'n':
        break

if len(valores) == 0:
    print("Nenhum valor para sacar! ")
else:
    for valor in valores:
        try:
            conta.saque(valor)
        except ValueError:
            print(f"Valor R${valor:.2f} inválido para o saque! \n")
        except SaldoInsuficiente as t:
            print(t)
        except:
            print("Ocorreu um erro no sistema. \n")
        else:
            print(f"Saque de R${valor:.2f} realizado com sucesso! \n")
        finally:
            print(f"Conexões finalizadas! Saldo atual: R${conta.saldo:.2f}.\n")