from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def atacar(self):
        pass

class Gato(Animal):
    def atacar(self):
        print("Arranhões!")

class Cachorro(Animal):
    def atacar(self):
        print("Mordida!")

class Tartaruga(Animal):
    def atacar(self):
        print("Rola na casca e ataca")

    def defender(self):
        print("Se esconder na casca")

if __name__ == '__main__':
    tartaruga = Tartaruga("Donatelo")
    gato = Gato("Garfield")
    cachorro = Cachorro("Rex")
    animais = [gato, cachorro, tartaruga]
    for animal in animais:
        animal.atacar()