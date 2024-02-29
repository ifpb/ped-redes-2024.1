from combustivel import Combustivel
from visor import Visor
from time import sleep
class BombaDeCombustivel:
    def __init__(self, combustivel1:Combustivel, combustivel2:Combustivel):
        self.preço_do_litro = [0.0, 0.0]
        self.combustivel = [combustivel1, combustivel2]
        self.litros_vendidos = [0.0, 0.0]
        self.total_vendido = [0.0, 0.0]
        self.visor = Visor()

    def alterar_preço(self, combustivel:Combustivel, preço:float):
        index = self.combustivel.index(combustivel)
        if preço > 0:
            self.preço_do_litro[index] = preço

    def preparar_abastecimento(self, combustivel:Combustivel):
        index = self.combustivel.index(combustivel)
        self.litros_vendidos[index] = 0.0
        self.total_vendido[index]   = 0.0
        self.visor.zerar()

    def abastecer_por_valor(self, combustivel:Combustivel, valor:float):
        index = self.combustivel.index(combustivel)
        if valor <= 0:
            return
        total = 0.0
        for litro in range(1, int(valor//self.preço_do_litro[index])+1):
            total += self.preço_do_litro[index]
            self.visor.set_visor(self.preço_do_litro[index], litro, total)
            self.visor.exibir()
            sleep(1)

        
        if valor > total: # tem sobra para ser contemplada
            sobra = valor - total
            litro += sobra/self.preço_do_litro[index]  
            total += sobra
            self.visor.set_visor(self.preço_do_litro[index], litro, total)
            self.visor.exibir()          
        



    # def abastecer_por_valor(self, valor):
    #     litros = valor / self.valor_litro
    #     self.quantidade_combustivel -= litros
    #     return litros

    # def abastecer_por_litro(self, litros):
    #     valor = litros * self.valor_litro
    #     self.quantidade_combustivel -= litros
    #     return valor

    # def alterar_valor(self, valor):
    #     self.valor_litro = valor

    # def alterar_combustivel(self, tipo_combustivel):
    #     self.tipo_combustivel = tipo_combustivel

    # def alterar_quantidade_combustivel(self, quantidade_combustivel):
    #     self.quantidade_combustivel = quantidade_combustivel

    def __str__(self):
        return f'''Bomba de combustível: 
combustivel1: {self.combustivel[0]} | Preço: {self.preço_do_litro[0]}
combustivel2: {self.combustivel[1]} | Preço: {self.preço_do_litro[1]}'''