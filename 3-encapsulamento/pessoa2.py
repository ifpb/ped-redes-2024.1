class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        assert type(novo_nome) == str, "Nome deve ser um string"
        self.__nome = novo_nome

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, nova_idade):
        assert type(nova_idade) == int, "Idade deve ser um número inteiro"
        self.__idade = nova_idade

try:
    p1 = Pessoa("Diego", 35)
    print("Idade = ", p1.idade)
    p1.idade = 36
    print("Idade = ", p1.idade)
except Exception as e:
    print(e)
