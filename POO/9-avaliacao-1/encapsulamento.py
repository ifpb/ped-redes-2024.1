class ContaEspecial:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial
    
    @property
    def saldo(self):
        return self.__saldo*0.10

class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial

    @property
    def saldo(self):
        return self.__saldo
    
    def deposito(self, valor):
        assert isinstance(valor, (int, float)), "Valor precisa ser numérico"
        assert valor > 0, "Valor precisa ser positivo"
        self.__saldo += valor

    def saque(self, valor):
        assert isinstance(valor, (int, float)), "Valor precisa ser numérico"
        assert valor > 0, "Valor precisa ser positivo"
        self.__saldo -= valor

class ContaPoupanca(ContaBancaria, ContaEspecial):
    def __init__(self, saldo_inicial=0, juros=0.005):
        super().__init__(saldo_inicial)
        self.juros = juros

    def rendimento(self):
        rendimento = self.saldo * self.juros
        self.deposito(rendimento)
        return rendimento

try:
    conta = ContaPoupanca(0, 0.005)
    conta.deposito(200)
    conta.saque(100)
    print("Saldo =",conta.saldo)
    print("Rendimento =",conta.rendimento())
except Exception as e:
    print(e)