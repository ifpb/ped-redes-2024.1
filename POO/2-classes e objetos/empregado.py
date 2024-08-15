class Empregado:

    num_empregados_criados = 0

    def __init__(self, nome, salario=1100.00):
        self.nome = nome
        self.salario_base = salario
        Empregado.num_empregados_criados += 1

    def __str__(self):
        return f"Nome = {self.nome}, Salário: {self.salario_base}"
    
    def calcular_salario_com_desconto(self):
        pass

    def desconto_vale_transporte(self):
        return self.salario_base * 0.06

e1 = Empregado("José da Silva", 3000)
print("Desconto do vale transporte=", e1.desconto_vale_transporte())
print("Nome do empregado =",e1.nome)
print("Salário do empregado =", e1.salario_base)
print("Empregados criados = ", Empregado.num_empregados_criados)
print("Empregado = ", e1)