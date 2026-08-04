from Jogo import *
listaPersonagens = []
while True:
    print("BEM VINDO AO X1 DE PERSONAGENS!")
    print("1- Criar um personagem")
    print("2- Criar um poder")
    print("3- Criar uma virtude")
    print("4- Fazer o x1")
    print("5- Mostrar personagens ")
    print("6- Sair")
    es = int(input("Digite o número correspondente à opção desejada: \n"))
    if es == 6:
        break
    
    elif es == 1:
        n = input("Digite o nome do personagem: \n")
        hv = int(input("Ele vai ser herói(1) ou vilão(2) ou normal(3)? \n"))
        if hv == 3:
            p = Personagem(n)
            listaPersonagens.append(p)
            print(f"Personagem {n} com vida {l} foi criado com sucesso!")
        elif p == 1:
            nR = input("Qual vai ser o nome real dele? \n")
            nPR = input("Qual o nome do par romântico? \n")
            p = Heroi(n, l, nR, nPR)
            listaPersonagens.append(p)
            print(f"Herói {n}({nR}) com vida {l} e par romântico {nPR} foi criado com sucesso!")
        elif p == 2:
            nC = int(input("Quantos crimes ele cometeu? \n"))
            p = Vilao(n, l, nC)
            listaPersonagens.append(p)
            print(f"Vilão {n} com vida {l} e com {nC} crimes cometidos foi criado com sucesso!")
            
    elif es == 5:
        if len(listaPersonagens) == 0:
            print("Você ainda não criou nenhum personagem!\n")
        else:
            for personagem in listaPersonagens:
                print(f"Nome: {personagem.nome}; Vida: {personagem.life}")