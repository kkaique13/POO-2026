#Importando as classes, função limpar terminal e conexão com o banco de dados
from Circulo import Circulo
from Quadrado import Quadrado
from func import limpar_terminal
from conexao import conectar
import pymysql

#Conectando o python com o banco de dados
conexao = conectar()

#Permitindo que o python possa mudar as coisas no banco de dados
banco = conexao.cursor()

if __name__ == "__main__":
    limpar_terminal()
    figuras = {}
    # Busca o maior número já cadastrado no banco e soma 1
    banco.execute("select coalesce(max(numero), 0) + 1 from Figura;")
    resultado = banco.fetchone()
    if resultado:
        numFigura = int(resultado[0])
    else:
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
                    banco.execute("insert into Figura values (%s, %s, %s);", (numFigura, "Círculo", corFigura))
                    banco.execute("insert into Circulo values (%s, %s);", (numFigura, medida))
                    conexao.commit()
                    numFigura += 1
                except ValueError:
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
                    banco.execute("insert into Figura values (%s, %s, %s);", (numFigura, "Quadrado", corFigura))
                    banco.execute("insert into Quadrado values (%s, %s);", (numFigura, medida))
                    conexao.commit()
                    numFigura += 1
                except ValueError:
                    print("Valor inválido! Digite um número real!")
                    continue
                
            #Inválido
            case _:
                print("Opção inválida. Tente novamente.")
                continue
            
        print("Figura cadastrada com sucesso!")
        resposta = input("Deseja cadastrar uma figura? (s/n)\n")
        limpar_terminal()
    
    try:
        banco.execute("""select f.numero, f.nomFigura, f.cor, c.raio
                        from Figura f, Circulo c
                        where f.numero = c.numFigura
                        union
                        select f.numero, f.nomFigura, f.cor, q.lado
                        from Figura f, Quadrado q
                        where f.numero = q.numFigura;""")
        
        for linha in banco.fetchall():
            valor = float(linha[3]) if linha[3] is not None else 0.0
            if linha[1].lower() == "círculo":
                print(f"Numero {linha[0]} | Figura: {linha[1]} | Cor: {linha[2]} | Raio: {valor:.2f}")
            elif linha[1].lower() == "quadrado":
                print(f"Numero {linha[0]} | Figura: {linha[1]} | Cor: {linha[2]} | Lado: {valor:.2f}")
        
    except pymysql.err.ProgrammingError as e:
        print(f"Erro de SQL ao consultar o banco: {e}")
        print("Procure o administrador!")
        
    except pymysql.err.OperationalError as e:
        print(f"Erro de conexão com o banco: {e}")
        
    except pymysql.err.MySQLError as e:
        print(f"Erro ao consultar o banco de dados: {e}")
        
    #Fechando o banco de dados
    banco.close()
    conexao.close()