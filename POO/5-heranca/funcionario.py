class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        assert isinstance(salario, (int, float)), 'Salário deve ser numérico'
        assert salario > 0, 'Salário deve ser maior que zero'
        self.__salario = salario

    def adiciona_aumento(self, valor):
        self.salario += valor

    def ganho_anual(self):
        return self.salario * 12
    
    def exibe_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Salário: R$ {self.salario:.2f}')
        print(f'Ganho anual: R$ {self.ganho_anual():.2f}')

class Assistente(Funcionario):
    def __init__(self, nome, salario, matricula):
        super().__init__(nome, salario)
        self.matricula = matricula
    
    def exibe_dados(self):
        super().exibe_dados()
        print(f'Matricula: {self.matricula}')

class Tecnico(Assistente):
    def __init__(self, nome, salario, matricula, bonus):
        super().__init__(nome, salario, matricula)
        self.bonus = bonus

    def ganho_anual(self):
        return super().ganho_anual() + self.bonus
    
    def exibe_dados(self):
        super().exibe_dados()
        print(f'\nBônus: R$ {self.bonus:.2f}')

class Administrativo(Assistente):
    def __init__(self, nome, salario, matricula, turno, adicional_noturno):
        super().__init__(nome, salario, matricula)
        self.turno = turno
        self.adicional_noturno = adicional_noturno

    def ganho_anual(self):
        return super().ganho_anual() + (self.adicional_noturno * 12)

    def exibe_dados(self):
        super().exibe_dados()
        print(f'\nTurno: {self.turno}' + f'\nAdicional noturno: R$ {self.adicional_noturno:.2f}')

if __name__ == '__main__':
    assistente = Assistente('Maria', 2000, 123)
    assistente.exibe_dados()
    print()
    tecnico = Tecnico('José', 3000, 456, 500)
    tecnico.exibe_dados()
    print()
    administrativo = Administrativo('Ana', 4000, 789, 'noturno', 100)
    administrativo.exibe_dados()
    print()