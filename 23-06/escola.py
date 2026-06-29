from datetime import date

class Presenca:
    def __init__(self, ID:int, data:str) -> None:
        self.ID = ID;
        self.data = data;

class Realiza:
    def __init__(self, est:Estudante, atv:Atividade) -> None:
        self.estudante = est;
        self.atividade = atv;
        self.nota = 0.0;
        self.estudante.addRealizacao(self);
        self.atividade.addRealizacao(self);
        
    def relatorio(self):
        print(f"Estudante: {self.estudante.nome}");
        print(f"{self.atividade.codigo} = {self.nota} pontos");
        
class Pessoa:
    def __init__(self, CPF:str, nome:str) -> None:
        self.CPF = CPF;
        self.nome = nome;
        self.listaFrequencia = [];
        
    def addPresenca(self, ID:int, data:date) -> None:
        self;listaPresenca.append(Presenca(ID, data));

class Docente(Pessoa):
    def __init__(self, CPF:str, nome:str, salario:float) -> None:
        super().__init__(CPF, nome);
        self.salario = salario;

class Estudante(Pessoa):
    def __init__(self, CPF:str, nome:str, RA:str) -> None:
        super().__init__(CPF, nome);
        self.RA = RA;
        self.realizacoes = [];

    def addRealizacao(self, realizacao:Realiza) -> None:
        self.realizacoes.append(realizacao);

class Atividade:
    def __init__(self, codigo:int, descricao:str, valor:float) -> None:
        self.codigo = codigo;
        self.descricao = descricao;
        self.valor = valor;
        self.realizacoes = [];
        
    def addRealizacao(self, realizacao:Realiza) -> None:
        self.realizacoes.append(realizacao);
