class Endereco:
    def __init__(self, rua, cidade, estado):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado

class Contato:
    def __init__(self, telefone, email):
        self.telefone = telefone
        self.email = email

class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco #1-1
        self.contatos = [] #1-N

if __name__ == '__main__':
    e = Endereco('Rua 1', 'Cidade 1', 'Estado 1')
    pessoa = Pessoa('João', e)
    print(pessoa.endereco.rua)
    print("Telefones da pessoa: ")
    for c in pessoa.contatos:
        print(c.telefone)