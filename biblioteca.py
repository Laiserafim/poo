class Pessoa():
    def __init__(self, nome, peso, idade, comendo= False, falando= False, dormindo=False):
        self.nome= nome #atributo
        self.peso= peso
        self.idade= idade
        self.comendo = False
        self.falando = False

    def comer (self,x):
        if self.falando:
            print(f"{self.nome} Não pode comer falando.")
            return

        if self.comendo:
            print(f"{self.nome} Já está comendo ")
            return

        print(f"{self.nome} está comendo {x}.")
        self.comendo = True

    def pararComer (self,x):
        if not self.comendo:
            print(f"{self.nome} Não está comendo.")
            return
        print(f"{self.nome} não está comendo")
        self.comendo = False

    def falar (self):
        if self.comendo:
            print(f"Não pode falar comendo.")
            return

        if self.falando:
            print(f"{self.nome} Já está falando")
            return
        print(f"{self.nome} está falando")
        self.falando = True

    def pararFalar (self):
        if not self.falando:
            print(f"{self.nome} Não está falando")
        print(f"{self.nome} parou de falar")
        self.falando = False

class Animal():
        def __init__(self,nome, cor):
            self.nome=nome
            self.cor=cor

        def comer(self):
            print(f"O {self.nome} foi comer...")

class Gato (Animal):
        def __init__(self,nome,cor):
            super(). __init__(nome,cor)

        def miar(self):
            print(f"O {self.nome} foi miando...")

class Cachorro (Animal):
    def __init__(self, nome,cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f"O {self.nome} late")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def cacareja(self):
        print(f"O {self.nome} cacareja")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def muge(self):
        print(f"O {self.nome} muge")

    def comeCapim(self):
        print(f"O {self.nome} come capim")

class Ingresso(): #classe
    def __init__(self,valor): #método construtor
        self.valor= valor

    def imprimeValor(self): #método
        print(f"O valor do ingresso é R$ {self.valor}. ")

class Vip(Ingresso):
    def __init__(self,valor):
        super().__init__(valor*1.5)

    def imprimeVip(self):
        print(f"O valor do ingresso vip é {self.valor:.2f}")


class Forma():
    def __init__(self):
        self.area= 0
        self.perimetro= 0

class Retangulo(Forma):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calcularArea(self):
        self.area = self.base * self.altura
        print(f"A base é {self.area}")

    def calcularPerimetro(self):
        self.perimetro = (self.base+self.altura)*2
        print(self.perimetro)

class Triangulo (Forma):
    def __init__(self, base, altura):
        super().__init__()
        self.base = base
        self.altura = altura

    def calcularArea(self):
        self.area = (self.base*self.altura)/2
        print(self.area)
    def calcularPerimetro(self):
        self.perimetro = self.base*3
        print(self.perimetro)



retangulo = Retangulo (2,2)
retangulo.calcularArea()
retangulo.calcularPerimetro()

triangulo = Triangulo(2,4)
triangulo.calcularArea()
triangulo.calcularPerimetro()