from random import choice

class Poder:
    def __init__(self, nome:str, nivelAtaque: float, nivelDefesa: float) -> None:
        self.nome = nome;
        self.nivelAtaque = nivelAtaque;
        self.nivelDefesa = nivelDefesa;

class Virtude:
    def __init__(self, nome:str, elemento:str, forca:int) -> None:
        self.__nome = nome;
        self.elemento = elemento;
        self.forca = forca;

    @property
    def nome(self) -> str:
        return self.__nome

class Personagem:
    def __init__(self, nome: str, life:float) -> None:
        self.nome = nome;
        self.life = 100.0;
        self.poderes = [];

    def addPoder(self, poder:Poder) -> None:
        self.poderes.append(poder);

    def usarPoder(self, ataque=False, defesa=False) -> Poder:
        if len(self.poderes) == 0:
            return None

        elif ataque:
            escolhido_ataque = self.poderes[0];
            for poder in self.poderes:
                if poder.nivelAtaque > escolhido_ataque.nivelAtaque:
                    escolhido_ataque = poder;
            return escolhido_ataque

        elif defesa:
            escolhido_defesa = self.poderes[0];
            for poder in self.poderes:
                if poder.nivelDefesa > escolhido_defesa.nivelDefesa:
                    escolhido_defesa = poder;
            return escolhido_defesa

        else:
            return choice(self.poderes)

class Vilao(Personagem):
    def __init__(self, nome:str, life:float, numeroCrimes:int) -> None:
        super().__init__(nome, life);
        self.__numeroCrimes = numeroCrimes;
    
    @property
    def numeroCrimes(self) -> int:
        return self.__numeroCrimes

    @numeroCrimes.setter
    def numeroCrimes(self, numeroCrimes:int) -> int:
        if numeroCrimes > self.__numeroCrimes:
            self.__numeroCrimes = numeroCrimes;
        return self.__numeroCrimes

    def usarPoder(self, ataque=False, defesa=False) -> Poder:
        pV = super().usarPoder(ataque, defesa);
        pV.nivelAtaque *= (1 + self.numeroCrimes/100)
        return pV

class Heroi(Personagem):
    def __init__(self, nome:str, life:float, nomeReal:str, nomeParR:str) -> None:
        super().__init__(nome, life);
        self.__nomeReal = nomeReal;
        self.nomeParRomantico = nomeParR;
        self.listaVirtudes = [];

    @property
    def nomeReal(self) -> str:
        return self.__nomeReal

    def addVirtudes(self, nomeVirtude:str, elemento:str, forca:int) -> None:
        self.listaVirtudes.append(Virtude(nomeVirtude, elemento, forca));

    def usarPoder(self, ataque=False, defesa=False) -> Poder:
        pH = super().usarPoder(ataque, defesa);
        return pH

    def tadeHack(self) -> None:
        pass
