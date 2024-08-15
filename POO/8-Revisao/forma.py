from abc import ABC, abstractmethod
from math import pi

class Forma(ABC):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass


class Retangulo(Forma):
    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return 2 * (self.largura + self.altura)

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return (2 * pi * self.raio) ** 2

    def perimetro(self):
        return (pi * self.raio) ** 2
    
if __name__ == '__main__':
    r = Retangulo(5, 10)
    c = Circulo(20)
    for f in [r, c]:
        print(f'Área do {f.__class__.__name__} = {f.area()}')
        print(f'Perímetro do {f.__class__.__name__} = {f.perimetro()}')
