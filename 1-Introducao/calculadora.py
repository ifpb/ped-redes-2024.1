class Calculadora:
    def __init__(self, registrador=0):
        self.registrador = registrador
        self.registrador_anterior = registrador
    
    def adicionar(self, valor):
        self.salvar_estado_anterior()
        self.registrador += valor

    def substrair(self, valor):
        self.salvar_estado_anterior()
        self.registrador -= valor

    def multiplicar(self, valor):
        self.salvar_estado_anterior()
        self.registrador *= valor

    def dividir(self, valor):
        if valor == 0:
            print("Não é possível dividir por zero")
        else:
            self.salvar_estado_anterior()
            self.registrador /= valor

    def reset(self):
        self.registrador = 0

    def undo(self):
        self.registrador, self.registrador_anterior = self.registrador_anterior, self.registrador

    def exibir(self):
        print(self)

    def __str__(self):
        return f"Registrador = {self.registrador}"

    def salvar_estado_anterior(self):
        self.registrador_anterior = self.registrador

c = Calculadora()
c.exibir()
c.adicionar(50)
c.multiplicar(10)
c.dividir(5)
c.substrair(35)
c.undo()
c.reset()
c.exibir()