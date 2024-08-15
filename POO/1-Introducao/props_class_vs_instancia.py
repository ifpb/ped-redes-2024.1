class Veiculo:

    MAX_VEICULOS = 2
    VEICULOS_CRIADOS = 0

    def __init__(self, marca, modelo, cor):
        if Veiculo.VEICULOS_CRIADOS >= Veiculo.MAX_VEICULOS:
            print("Criação de veículos atingiu o limite!")
        else:
            self.marca = marca
            self.modelo = modelo
            self.cor = cor
            self.__velocidade = 0
            Veiculo.incrementar_veiculo_criado()

    @staticmethod
    def incrementar_veiculo_criado():
        Veiculo.VEICULOS_CRIADOS += 1
    
    @property
    def velocidade(self):
        self.__velocidade

    @velocidade.setter
    def velocidade(self, velocidade):
        if velocidade > 120:
            print("Velocidade Máxima Excedida!")
        else:
            self.__velocidade = velocidade



    def acelerar(self):
        self.acelerou = True
        self.__velocidade += 10

    def reduzir(self):
        if self.__velocidade <= 10:
            self.parar()
        else:
            self.__velocidade -= 10

    def parar(self):
        self.__velocidade = 0

    def __str__(self):
        return f"Marca={self.marca}, Modelo={self.modelo}, Cor={self.cor}, Velocidade={self.__velocidade}"

v1 = Veiculo("Fiat", "Uno", "Preta")
print("V1=",v1)
v1.velocidade = 200
v1.acelerar()
v1.acelerar()
v1.acelerar()
v1.reduzir()
print("Velocidade V1 =",v1.velocidade)
v2 = Veiculo("VW", "Polo", "Branca")
print("V2=",v2)
v3 = Veiculo("Ford", "Focus", "Cinza")