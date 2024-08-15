from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frear(self):
        pass

    @abstractmethod
    def obter_tipo_combustivel(self):
        return 'Gasolina'

class Carro(Veiculo):
    def acelerar(self):
        return 'Vrruuuum'
    
    def frear(self):
        return 'Freandooooooo'
    
    def obter_tipo_combustivel(self):
        return super().obter_tipo_combustivel()
    
class Bicicleta(Veiculo):
    def acelerar(self):
        return 'Pedalandoo'
    
    def frear(self):
        return 'Apertando o freio'
    
    def obter_tipo_combustivel(self):
        return 'Força humana'
    
if __name__ == '__main__':
    c = Carro('Fuscao Preto')
    b = Bicicleta('Caloi')
    for v in [c, b]:
        print(f'Dados da classe {v.__class__.__name__}:')
        print(v.acelerar())
        print(v.frear())
        print(v.obter_tipo_combustivel())