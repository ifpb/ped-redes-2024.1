class ValorInvalido(Exception):
    def __init__(self, msg, obj_fonte):
        super().__init__(msg)
        self.obj_fonte = obj_fonte

class Pessoa:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.__atribuir_salario(salario)      

    def __atribuir_salario(self, salario):
        assert type(salario) == int or type(salario) == float, "Valor do salário deve ser inteiro ou float"
        assert salario > 0, "Valor do salário deve ser maior que zero"
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario
    
    def aumentar_salario(self, valor):
        assert type(valor) == int or type(valor) == float, "Valor a aumentar deve ser inteiro ou float"
        assert valor > 0, "Valor a aumentar deve ser maior que zero"
        self.__salario += valor

    @property 
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        assert type(nome) == str, "Nome deve ser uma string"
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        assert type(idade) == int, "Idade deve ser um inteiro"
        assert 0 <= idade <= 100, "Idade deve ser entre 0 e 100"
        self.__idade = idade

if __name__ == '__main__':
    try:
        p = Pessoa("José da Silva", 30, 3000)
        p.aumentar_salario(100)
        print(f"Salário de {p.nome} = {p.salario}")
        p2 = Pessoa("Maria Bezerra", 90, 5000)
        p2.aumentar_salario(500)
        print(f"Salário de {p2.nome} = {p2.salario}")
    except AssertionError as e:
        print(e)