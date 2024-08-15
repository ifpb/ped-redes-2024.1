from abc import ABC, abstractmethod
from enum import Enum

class GrauInstrucao(Enum):
    GRADUADO = "Graduado"
    ESPECIALISTA = "Especialista"
    MESTRE = "Mestre"
    DOUTOR = "Doutor"

class Funcionario(ABC):
    def __init__(self, nome, salario, grau_instrucao=GrauInstrucao.GRADUADO):
        self.nome = nome
        self.salario = salario
        self.grau_instrucao = grau_instrucao

    @abstractmethod
    def add_bonificacao(self):
        pass

    def contracheque(self):
        return self.salario + self.add_bonificacao()

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, n):
        self.__nome = n

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, s):
        assert type(s) == int or type(s) == float, "Salário precisa ser um número"
        assert s >= 0, "Salário precisa ser um número positivo"
        self.__salario = s
        
    @property
    def grau_instrucao(self):
        return self.__grau_instrucao
    
    @grau_instrucao.setter
    def grau_instrucao(self, g):
        assert type(g) == GrauInstrucao, "Grau de instrução precisa ser uma enumeração do tipo GrauInstrucao"
        self.__grau_instrucao = g

    def __str__(self):
        return f"""
        Sou um objeto da class: {self.__class__.__name__},
        Nome: {self.nome},
        Salário: {self.salario},
        Grau de instrução: {self.grau_instrucao.value},
        Contracheque: {self.contracheque()}
        """

class Gerente(Funcionario):

    def adicional_qualificacao(self):
        if self.grau_instrucao == GrauInstrucao.ESPECIALISTA:
            return self.salario * 0.15
        elif self.grau_instrucao == GrauInstrucao.MESTRE:
            return self.salario * 0.25
        elif self.grau_instrucao == GrauInstrucao.DOUTOR:
            return self.salario * 0.50
        return 0

    def add_bonificacao(self):
        return (self.salario * 0.30) + self.adicional_qualificacao()

class Diretor(Gerente):
    def add_bonificacao(self):
        return self.adicional_qualificacao() 

class Presidente(Funcionario):
    def add_bonificacao(self):
        bonus = self.salario * 2
        if self.grau_instrucao == GrauInstrucao.DOUTOR:
            bonus = self.salario * 4
        return bonus

if __name__ == '__main__':
    diretor = Diretor("Steve Jobs", 10000, GrauInstrucao.MESTRE)
    print("Diretor =", diretor)
    presidente = Presidente("Bill Gates", 10000, GrauInstrucao.GRADUADO)
    print("Presidente =", presidente)
    gerente = Gerente("Linus Torvalds", 10000, GrauInstrucao.DOUTOR)
    print("Gerente =", gerente)

    funcionarios = [diretor, presidente, gerente]
    for funcionario in funcionarios:
        print("Nome =", funcionario.nome)
        print("Contracheque =", funcionario.contracheque())
        print("Salário base =", funcionario.salario)
        print("Bonificação =", funcionario.add_bonificacao())


