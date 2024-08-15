class IdadeInvalida(Exception):
    pass

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        if self.idade > 100:
            raise IdadeInvalida("Idade não pode ser maior do que 100")
try:
    pessoa = Pessoa('Diego', 101)
except IdadeInvalida as e:
    print(e)
except Exception as e:
    print("Forneça um número válido como idade")
print('Encerrando o programa')