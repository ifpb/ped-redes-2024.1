class Carro:
    def __init__(self, modelo, placa, ano, valor):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.valor = valor
    
    def __str__(self):
        props = self.__dict__
        resultado = ""
        for k, v in props.items():
            resultado += f"{k} = {v}\n"
        return resultado

class Pessoa:
    def __init__(self, nome, endereco, nascimento, veiculo):
        self.nome = nome
        self.endereco = endereco
        self.nascimento = nascimento
        self.veiculo = veiculo

    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, v):
        assert type(v) == Carro, "O veículo deve ser um objeto do tipo carro"
        self.__veiculo = v

try:
    c = Carro("VW Polo", "XXX-XXXX", 2023, 60.000)
    print(c)
    p = Pessoa("Diego", "Rua X", "12/06/1988", c)
    print(f"O carro de {p.nome} é: {p.veiculo.modelo}")
except AssertionError as e:
    print(e)