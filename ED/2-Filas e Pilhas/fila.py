from no import No


class FilaVaziaException(Exception):
    def __init__(self, msg):
        self.msg = msg


class Fila:
    def __init__(self):
        self.__inicio = None
        self.__fim = None

    def add(self, valor):
        novo = No(valor)

        if self.is_empty():  ## Fila vazia
            self.__inicio = self.__fim = novo
        else:
            self.__fim.prox = novo
            self.__fim = novo
            

    def remove(self):
        if self.is_empty():
            raise FilaVaziaException("Fila vazia, não é possível remover!")

        elemento = self.__inicio
        self.__inicio = self.__inicio.prox
        return elemento

    def is_empty(self):
        return self.__inicio is None and self.__fim is None

    def __str__(self):
        return "[%s]" % self.__inicio