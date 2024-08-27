from no import No


class PilhaVaziaException(Exception):
    def __init__(self, msg):
        self.msg = msg


class Pilha:
    def __init__(self):
        self.topo = None

    @property
    def topo(self):
        return self.__topo

    @topo.setter
    def topo(self, topo):
        assert isinstance(topo, No) or topo is None,  "O topo deve ser do tipo No ou None"
        self.__topo = topo

    def push(self, valor):
        novo = No(valor)
        # Caso 1 - Pilha vazia
        if self.is_empty():
            self.__topo = novo
            return
        # Caso 2 - Pilha com ao menos um elemento
        novo.prox = self.__topo
        self.__topo = novo

    def pop(self):
        # Caso 1 - Pilha vazia
        if self.is_empty():
            raise PilhaVaziaException("Pilha vazia, não foi possível remover!")
        # Caso 2 - Pilha com ao menos um elemento
        elemento = self.__topo
        self.__topo = self.__topo.prox
        return elemento

    def remover_ate_elemento(self, elemento):
        while self.pop().carga != elemento:
            pass
        if self.topo.carga == elemento:
            self.pop()

    def is_empty(self):
        return self.__topo is None

    def __str__(self):
        return "[%s]" % self.__topo