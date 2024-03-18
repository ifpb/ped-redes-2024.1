class Conta:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.__saldo = saldo
        self.titular = titular

    def sacar(self, valor):
        assert type(valor) == int or type(valor) == float, "Valor passado deve ser um número"
        assert valor > 0, "O valor do saque deve ser maior do que 0"
        assert self.__saldo >= valor, "Saldo insuficiente"
        self.__saldo -= valor

    def depositar(self, valor):
        assert type(valor) == int or type(valor) == float, "Valor passado deve ser um número"
        assert valor > 0, "O valor do depósito deve ser maior do que 0"
        self.__saldo += valor

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, n):
        self.__numero = n

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, t):
        self.__titular = t

    def __str__(self):
        return f"Conta: {self.numero}, Titular: {self.titular}, Saldo: {self.saldo}"

if __name__ == '__main__':
    print("Bem-vindos ao programa de contas bancárias")
    print("Vamos criar a sua conta!")
    numero_conta = input("Digite o número da conta")
    titular = input("Digite o nome do titular")
    c = Conta(numero_conta, titular)

    while True:
        print("Opções disponíveis")
        print("1 - depositar")
        print("2 - sacar")
        print("3 - saldo")
        print("4 - encerrar o programa")

        opcao = 0
        try:
            opcao = int(input("Digite a opção desejada: "))
        except:
            print("Opção inválida")
            continue

        if opcao == 1:
            try:
                valor = float(input("Digite o valor que deseja depositar: "))
                c.depositar(valor)
            except AssertionError as e:
                print(e)
            except ValueError as e:
                print("O valor deve ser do tipo float ou int")
        elif opcao == 2:
            try:
                valor = float(input("Digite o valor que deseja sacar: "))
                c.sacar(valor)
            except AssertionError as e:
                print(e)
            except ValueError as e:
                print("O valor deve ser do tipo float ou int")
        elif opcao == 3:
            print("Saldo da conta = ", c.saldo)
        elif opcao == 4:
            print("Obrigado por usar o nosso programa")
            break
        else:
            print("Opção inválida")

