class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.set_idade(idade)

    def get_idade(self):
        return self.__idade
    
    def set_idade(self, nova_idade):
        assert type(nova_idade) == int, "Idade deve ser um número inteiro"
        self.__idade = nova_idade

p1 = Pessoa("Diego", 35)
print("Idade = ", p1.get_idade())
p1.set_idade(36)
print("Idade = ", p1.get_idade())
