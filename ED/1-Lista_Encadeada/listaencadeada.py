class No:
    def __init__(self, carga, prox=None):
        self.carga = carga
        self.prox = prox

    @property
    def carga(self):
        return self.__carga

    @carga.setter
    def carga(self, carga):
        self.__carga = carga

    @property
    def prox(self):
        return self.__prox

    @prox.setter
    def prox(self, prox):
        assert isinstance(prox, No) or prox is None, "O próximo nó precisa ser um objeto do tipo No ou None"
        self.__prox = prox

    def __str__(self):
        if self.__prox is None:
            return '%s' % self.__carga
        else:
            return '%s -> %s' % (self.__carga, self.__prox)


class ListaEncadeadaException(Exception):
    def __init__(self, msg):
        self.msg = msg


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    @property
    def cabeca(self):
        return self.__cabeca

    @cabeca.setter
    def cabeca(self, cabeca):
        assert isinstance(cabeca, No) or cabeca is None, "A cabeça precisa ser um objeto do tipo No ou None"
        self.__cabeca = cabeca

    @property
    def cauda(self):
        return self.__cauda

    @cauda.setter
    def cauda(self, cauda):
        assert isinstance(cauda, No) or cauda is None, "A cauda precisa ser um objeto do tipo No ou None"
        self.__cauda = cauda

    def esta_vazia(self):
        return self.__cabeca is None

    def inserir_no_inicio(self, valor):
        """Insere um novo valor no início da lista encadeada
        Caso 1: lista vazia - o novo nó será atribuído como cabeça e cauda
        Caso 2: lista com um ou mais elementos - o novo nó será atribuído como cabeça da lista
        :param valor valor do novo item a ser inserido na lista
        :type valor object
        """
        novo = No(valor)
        if self.esta_vazia():
            self.__cabeca = self.__cauda = novo
        else:
            novo.prox = self.__cabeca
            self.__cabeca = novo

    def inserir_no_final(self, valor):
        """Insere um novo valor no final da lista encadeada
        Caso 1: lista vazia - o novo nó será atribuído como cabeça e cauda
        Caso 2: lista com um ou mais elementos - o novo nó será atribuído como cabeça da lista
        :param valor valor do novo item a ser inserido na lista
        :type valor object
        """
        novo = No(valor)
        if self.esta_vazia():
            self.__cabeca = self.__cauda = novo
        else:
            self.__cauda.prox = novo
            self.__cauda = novo

    def remover_do_inicio(self):
        """Remove o elemento do início da lista encadeada
        Caso 1: lista vazia - é lançada uma ListaEncadeadaException, pois não há nada a remover
        Caso 2: lista com apenas um elemento - a cabeça e cauda da lista são atribuídas a None
        Caso 3: lista com mais de um elemento - a cabeça é atribuída ao próximo elemento da cabeça atual
        """
        if self.esta_vazia():
            raise ListaEncadeadaException("Lista está vazia!")
        if self.__cabeca == self.__cauda:
            self.__cabeca = self.__cauda = None
        else:
            self.__cabeca = self.__cabeca.prox

    def __str__(self):
        """Retorna uma string formada com todos os elementos da lista encadeada
        """
        return "[%s]" % self.__cabeca

    def remover_do_final(self):
        """Remove o elemento do final da lista encadeada
        Caso 1: lista vazia - é lançada uma ListaEncadeadaException, pois não há nada a remover
        Caso 2: lista com apenas um elemento - a cabeça e cauda da lista são atribuídas a None
        Caso 3: lista com mais de um elemento - a cauda é atribuída ao penúltimo elemento da lista atual
        """
        if self.esta_vazia():
            raise ListaEncadeadaException("Lista está vazia!")
        if self.__cabeca == self.__cauda:
            self.__cabeca = self.__cauda = None
        else:
            atual = self.__cabeca
            while atual is not None and atual.prox is not self.cauda:
                atual = atual.prox

            if atual is not None:
                atual.prox = None
            self.__cauda = atual