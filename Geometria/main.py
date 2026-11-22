#Importando as classes e função limpar terminal
from Circulo import Circulo
from Quadrado import Quadrado
from func import limpar_terminal

from conexao import conectar

conexao = conectar()
banco = conexao.cursor()

if __name__ == "__main__":
    limpar_terminal()
    figuras = {}
    numFigura = 1
    print("CADASTRO DE FIGURAS\n")
    resposta = input("Deseja cadastrar uma figura? (s/n)\n")
    while resposta.lower() == "s":
        # Menu de opções
        tipoFigura = int(input("Qual figura?\n1- Círculo\n2- Qudrado\n"))
        match tipoFigura:
            #Círculo
            case 1:
                corFigura = input("Informe a cor da figura: \n")
                #Caso de excessão para caso a pessoa digitar um valor inválido para o raio, mostrará uma mensagem de erro e pedirá para digitar novamente.
                try:
                    medida = float(input("Qual o valor do raio?\n"))
                    if medida <= 0:
                        print("Valor inválido. O raio deve ser maior que zero.")
                        continue
                    
                    figuras[f"Figura {numFigura}"] = Circulo(corFigura, medida)
                    banco.execute(f"insert into Figura values ({numFigura}, '{corFigura}');")
                    banco.execute(f"insert into Circulo values ({numFigura}, {medida:.2f});")
                    banco.execute("commit;")
                    numFigura += 1
                except ValueError:
                    limpar_terminal()
                    print("Valor inválido! Digite um número real!")
                    continue
                
            #Quadrado
            case 2:
                corFigura = input("Informe a cor da figura: \n")
                #Caso de excessão para caso a pessoa digitar um valor inválido para o lado, mostrará uma mensagem de erro e pedirá para digitar novamente.
                try:
                    medida = float(input("Qual o valor do lado?\n"))
                    if medida <= 0:
                        print("Valor inválido. O lado deve ser maior que zero.")
                        continue
                    
                    figuras[f"Figura {numFigura}"] = Quadrado(corFigura, medida)
                    banco.execute(f"insert into Figura values ({numFigura}, {medida:.2f});")
                    numFigura += 1
                except ValueError:
                    limpar_terminal()
                    print("Valor inválido! Digite um número real!")
                    continue
                
            #Inválido
            case _:
                print("Opção inválida. Tente novamente.")
                continue
            
        print("Figura cadastrada com sucesso!")
        resposta = input("Deseja cadastrar uma figura? (s/n)\n")
        limpar_terminal()
    
    #Retornando os dados
    for chave in figuras:
        print(figuras[chave].retornarDados())
    
    #Fechando o banco de dados
    conexao.close()