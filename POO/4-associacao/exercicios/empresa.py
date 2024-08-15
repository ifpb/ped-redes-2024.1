from datetime import datetime

class Funcionario:
    def __init__(self, nome, cpf, cargo, empresa):
        self.nome = nome
        self.cargo = cargo
        self.cpf = cpf
        self.empresa = empresa

    @property
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, empresa):
        assert isinstance(empresa, Empresa), 'A empresa deve ser uma instância de Empresa'
        self.__empresa = empresa

class Empresa:
    def __init__(self, nome):
        self.nome = nome

class Presenca:
    def __init__(self, funcionario, data=datetime.now()):
        self.funcionario = funcionario
        self.data = data

    @property
    def funcionario(self):
        return self.__funcionario
    
    def funcionario(self, f):
        assert isinstance(f, Funcionario), 'O funcionário deve ser uma instância de Funcionario'
        self.__funcionario = f

if __name__ == '__main__':
    empresa = Empresa('ACME')
    funcionario = Funcionario('João', '123.456.789-00', 'Analista', empresa)
    presenca = Presenca(funcionario)
    print(presenca.funcionario.empresa.nome)