from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f'{self.nome} - Área: {self.area()} - Perímetro: {self.perimetro()}'

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        super().__init__('Quadrado')
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado
    
class Triangulo(FormaGeometrica):
    def __init__(self, base, altura, lado1, lado2):
        super().__init__('Triângulo')
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def area(self):
        return (self.base * self.altura) / 2

    def perimetro(self):
        return self.base + self.lado1 + self.lado2
    

class Circulo:
    def __init__(self, raio, nome):
        self.raio = raio
        self.nome = nome

    def area(self):
        return 3.14 * self.raio ** 2

    def perimetro(self):
        return 2 * 3.14 * self.raio

    def __str__(self):
        return f'{self.nome} - Área: {self.area()} - Perímetro: {self.perimetro()}'


if __name__ == '__main__':
    FormaGeometrica.register(Circulo)
    q = Quadrado(5)
    print(isinstance(q, FormaGeometrica))
    t = Triangulo(3, 4, 5, 5)
    print(isinstance(t, FormaGeometrica))
    c = Circulo(3, "circulo")
    print(isinstance(c, FormaGeometrica))
    formas = [q, t, c]
    for forma in formas:
        print(forma)