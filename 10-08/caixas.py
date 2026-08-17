from random import *

def mostrarLista(inicio):
    aux = inicio
    while aux is not None:
        numero = aux.valor
        print(f"| {(numero if numero >= 10 else '0' + str(numero)):2.0f} |-->", end="")
        aux = aux.setinha
    print("| | |")

class Caixa:
    def __init__(self, numero, setinha):
        self.numero = numero
        self.setinha = setinha

while True:
    try:    
        q = int(input("Até quantas caixas? "))
        n = randint(1, q)
        break
    except:
        print("Valor inválido! ")


inicio = Caixa(1, None)
final = inicio

for numero in range(2, n + 1):
    final.setinha = Caixa(randint(0, 99), None)
    final = final.setinha
mostrarLista(inicio)

numAtual = int(input("Qual número quer atualizar? "))
aux = inicio
while aux is not None:
    if aux.valor == numAtual:
        aux.valor = aux.valor ** 2
    aux = aux.setinha
mostrarLista(inicio)

numExcluir = int(input("Qual número excluir? "))
while inicio is not None and inicio.valor == numExcluir:
    inicio = inicio.setinha
aux = inicio
if aux is not None:
    while aux.setinha is not None and aux.setinha.valor == numExcluir:
        aux.setinha = aux.setinha.setinha
mostrarLista(inicio)
