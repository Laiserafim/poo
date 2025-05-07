class Pessoa():
    def __init__(self, nome, peso, idade, comendo= False, falando= False, dormindo=False):
        self.nome= nome
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


