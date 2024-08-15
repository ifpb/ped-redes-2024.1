class SalarioExcedente(Exception):
    pass

class Pessoa:

    VALOR_MAXIMO = 5000

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario
        self.verifica_valor_maximo()
    
    def verifica_valor_maximo(self):
        if self.salario > self.VALOR_MAXIMO:
            raise SalarioExcedente("Salário maior do que o limite")
            
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, n):
        self.__nome = n

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, i):
        assert type(i) == int, "Idade deve ser um inteiro"
        assert 0 <= i <= 100, "Idade inválida"
        self.__idade = i

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, s):
        assert type(s) == int or type(s) == float, "Salário deve ser um número"
        assert s > 0, "Salário deve ser maior que 0"
        self.__salario = s
        self.verifica_valor_maximo()

try:
    pessoa = Pessoa('Diego', 30, 5000)
    pessoa.salario = 100000
except AssertionError as e:
    print(e)
except SalarioExcedente as e:
    print(e)
print('Encerrando o programa')