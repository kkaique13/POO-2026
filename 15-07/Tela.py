from Jogo import *
listaPersonagens = []
listaPoderes = []
listaVirtudes = []

while True:
    print("BEM VINDO AO X1 DE PERSONAGENS!")
    print("1- Criar um personagem")
    print("2- Criar um poder")
    print("3- Criar uma virtude")
    print("4- Fazer o x1")
    print("5- Mostrar personagens ")
    print("6- Mostrar Poderes")
    print("7- Mostrar Virtudes")
    print("8- Sair")
    es = int(input("Digite o número correspondente à opção desejada: \n"))
    
    #Sair
    if es == 8:
        break

    #Personagem
    elif es == 1:
        n = input("Digite o nome do personagem: \n")
        l = 100.0
        hv = int(input("Ele vai ser herói(1) ou vilão(2) ou normal(3)? \n"))
        if hv == 3:
            pe = Personagem(n, l)
            listaPersonagens.append(pe)
            print(f"Personagem {n} com vida {l:.2f} foi criado com sucesso!")
        elif hv == 1:
            nR = input("Qual vai ser o nome real dele? \n")
            nPR = input("Qual o nome do par romântico? \n")
            pe = Heroi(n, l, nR, nPR)
            listaPersonagens.append(pe)
            print(f"Herói {n}({nR}) com vida {l:.2f} e par romântico {nPR} foi criado com sucesso!")
        elif hv == 2:
            nC = int(input("Quantos crimes ele cometeu? \n"))
            pe = Vilao(n, l, nC)
            listaPersonagens.append(pe)
            print(f"Vilão {n} com vida {l:.2f} e com {nC} crimes cometidos foi criado com sucesso!")
            
    elif es == 5:
        if len(listaPersonagens) == 0:
            print("Você ainda não criou nenhum personagem!\n")
        else:
            for personagem in listaPersonagens:
                print(f"Nome: {personagem.nome}; Vida: {personagem.life}; Poderes: {personagem.poderes}")
                if isinstance(personagem, Heroi):
                    print(f"Nome de herói: {personagem.nome};\n Nome real: {personagem.nomeReal};\n Vida: {personagem.life};\n Par romântico: {personagem.nomeParRomantico};\n Poderes: {personagem.poderes}; Virtudes: {personagem.listaVirtudes}")
                if isinstance(personagem, Vilao):
                    print(f"Nome de vilão: {personagem.nome};\n Vida: {personagem.life};\n Número de crimes cometidos: {personagem.numeroCrimes};\n Poderes: {personagem.poderes}")

    #Poderes
    elif es == 2:
        nP = input("Digite o nome do poder: ")
        nA = float(input("Digite o nível de ataque do poder: \n"))
        nD = float(input("Digite o nível de defesa do poder: \n"))
        po = Poder(nP, nA, nD)
        listaPoderes.append(po)
        print(f"Poder {nP} com ataque {nA:.2f} e defesa {nD:.2f} criado com sucesso!")
        if len(listaPersonagens) == 0:
            print("Crie um personagem para adicionar o poder aqui direto!")
        else:
            ap = input("Gotaria de adicionar este poder a um personagem? (s/n)\n")
            while ap == "s":
                for personagem in listaPersonagens:
                    print(personagem.nome)
                    pope = input("Para qual personagem você quer colocar o poder? \n")
                    if pope != personagem.nome:
                        pope = input("Personagem não existe, tente novamente! \n")
                    else:
                        personagem.addPoder(po)
                ap = input("Gotaria de adicionar este poder a um personagem? (s/n)\n")
    
    elif es == 6:
            if len(listaPoderes) == 0:
                print("Você ainda não criou nenhum poder!\n")
            else:
                for poder in listaPoderes:
                    print(f"Nome: {poder.nome}; Ataque: {poder.nivelAtaque}; Defesa: {poder.nivelDefesa}")
    
    #Virtudes
    elif es == 3:
        nV = input("Digite o nome da virtude: \n")
        eV = input("Digite o elemento da virtude: \n")
        fV = int(input("Digite a força da virtude: \n"))
        vi = Virtude(nV, eV, fV)
        listaVirtudes.append(vi)
        print(f"Virtude {nV} com elemento {eV} e força {fV} criada com sucesso!")
        if len(listaPersonagens) == 0:
            print("Crie um personagem para adicionar a virtude aqui direto!")
        else:
            av = input("Gotaria de adicionar esta virtude a um herói? (s/n)\n")
            while av == "s":
                for personagem in listaPersonagens:
                    if isinstance(personagem, Heroi):
                        print(personagem.nome)
                        vihe = input("Para qual herói você quer colocar a virtude? \n")
                        if vihe != personagem.nome:
                            vihe = input("Herói não existe, tente novamente! \n")
                        else:
                            personagem.addVirtudes(nV, eV, fV)
                    else:
                        print(f"{personagem.nome} não é um herói!")
                av = input("Gotaria de adicionar esta virtude a um herói? (s/n)\n")
                
    elif es == 7:
            if len(listaVirtudes) == 0:
                print("Você ainda não criou nenhuma virtude!\n")
            else:
                for virtude in listaVirtudes:
                    print(f"Nome: {virtude.nome}; Elemento: {virtude.elemento}; Força: {virtude.forca}")

    #x1
    elif es == 4:
        for personagem in listaPersonagens:
            print(personagem.nome)
            per1 = input("Insira o nome do primeiro personagem: \n")
            per2 = input("Insira o nome do segundo personagem: \n")
            if per1 != personagem.nome or per2 != personagem.nome:
                print("Personagem inválido! Tente novamente")