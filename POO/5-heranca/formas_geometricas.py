class FormaGeometrica:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def perimetro(self):
        return 2 * (self.largura + self.altura)

class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura, cor):
        self.cor = cor
        super().__init__(largura, altura)

    def area(self):
        return self.largura * self.altura

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        super().__init__(lado, lado)
    
    def area(self):
        return self.largura ** 2

class Triangulo(FormaGeometrica):
    def area(self):
        return (self.largura * self.altura) / 2
     
if __name__ == '__main__':
    retangulo = Retangulo(10, 5)
    print(retangulo.area())
    print(retangulo.perimetro())
    quadrado = Quadrado(5)
    print(quadrado.area())
    print(quadrado.perimetro())