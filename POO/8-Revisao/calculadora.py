from numbers import Number
from functools import reduce

class ZeroMultiplicationError(Exception):
    pass

class CalculadoraRobusta:
    def __init__(self, numeros):
        self.numeros = numeros

    def somar(self):
        return reduce(lambda x,y: x+y, self.numeros)

    def subtrair(self):
        return reduce(lambda x,y: x-y, self.numeros)
    
    def multiplicar(self):
        if 0 in self.numeros:
            raise ZeroMultiplicationError('Não é possível multiplicar por zero')
        return reduce(lambda x,y: x*y, self.numeros)
    
    def dividir(self):
        return reduce(lambda x,y: x/y, self.numeros)

class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    @property
    def num1(self):
        return self.__num1

    def num1(self, num1):
        assert isinstance(num1, Number), "Num1 deve ser um número"
        self.__num1 = num1

    @property    
    def num2(self):
        return self.__num2

    def num2(self, num2):
        assert isinstance(num2, Number), "Num2 deve ser um número"
        self.__num2 = num2

    def somar(self):
        return self.num1 + self.num2

    def subtrair(self):
        return self.num1 - self.num2
    
    def multiplicar(self):
        if self.num1 == 0 or self.num2 == 0:
            raise ZeroMultiplicationError('Não é possível multiplicar por zero')
        return self.num1 * self.num2
    
    def dividir(self):
        return self.num1 / self.num2


if __name__ == '__main__':
    try: 
        # c = Calculadora(5, 0)
        c = CalculadoraRobusta([2, 3, 4, 5, 6, 10, 44])
        print("soma =", c.somar())
        print("subtracao =", c.subtrair())
        print("multiplicacao =", c.multiplicar())
        print("divisao =", c.dividir())
    except AssertionError as e:
        print(e)
    except ZeroDivisionError:
        print('Não é possível dividir por zero')
    except ZeroMultiplicationError as e:
        print(e)
    except Exception:
        print('Erro desconhecido!')