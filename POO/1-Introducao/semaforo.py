from enum import Enum
from time import sleep

class Cor(Enum):
    VERMELHO = 'VERMELHO'
    AMARELO = 'AMARELO'
    VERDE = 'VERDE'
    

class Semaforo:
    def __init__(self, cor=Cor.VERMELHO, temporizador=10):
        self.cor = cor
        self.temporizador = temporizador
        self.mudar_cor()

    def mudar_cor(self):
        while self.temporizador > 0:
            print("Cor:", self.cor.value, "Temporizador:", self.temporizador)
            self.temporizador -= 1
            sleep(1)
        if self.cor == Cor.VERMELHO:
            self.cor = Cor.VERDE
            self.temporizador = 20
        elif self.cor == Cor.VERDE:
            self.cor = Cor.AMARELO
            self.temporizador = 3
        elif self.cor == Cor.AMARELO:
            self.cor = Cor.VERMELHO
            self.temporizador = 10
        self.mudar_cor()

semaforo = Semaforo()
