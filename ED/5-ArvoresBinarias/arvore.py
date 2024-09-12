## Árvore Binária
class No:
    def __init__(self, carga: object, esquerda: 'No' = None, direita: 'No' = None):
        self.carga = carga
        self.esquerda = esquerda
        self.direita = direita

    def __str__(self):
        return str(self.carga)


RAIZ = "raiz"


class ArvoreBinaria:
    def __init__(self, raiz: 'No'):
        self.raiz = raiz

    def pos_ordem(self, no: 'No' = RAIZ):
        if no == RAIZ:
            no = self.raiz
        if no is None:
            return no
        if no.esquerda:
            self.pos_ordem(no.esquerda)
        if no.direita:
            self.pos_ordem(no.direita)
        print(no, end=" ")

    def em_ordem(self, no: 'No' = RAIZ):
        if no == RAIZ:
            no = self.raiz
        if no is None:
            return no
        if no.esquerda:
            self.em_ordem(no.esquerda)
        print(no, end=" ")
        if no.direita:
            self.em_ordem(no.direita)

    def pre_ordem(self, no: 'No' = RAIZ):
        if no == RAIZ:
            no = self.raiz
        if no is None:
            return no
        print(no, end=" ")
        if no.esquerda:
            self.pre_ordem(no.esquerda)
        if no.direita:
            self.pre_ordem(no.direita)


class ArvoreBinariaBusca(ArvoreBinaria):

    def inserir(self, no, raiz=RAIZ):
        if raiz == RAIZ:
            raiz = self.raiz

        if raiz is None:
            raiz = no
        elif no.carga > raiz.carga:
            if raiz.direita is None:
                raiz.direita = no
            else:
                self.inserir(no, raiz.direita)
        elif no.carga < raiz.carga:
            if raiz.esquerda is None:
                raiz.esquerda = no
            else:
                self.inserir(no, raiz.esquerda)

    def buscar(self, chave, raiz=RAIZ):
        if raiz == RAIZ:
            raiz = self.raiz

        if raiz is None:
            return None

        if raiz.carga == chave:
            return raiz

        if chave > raiz.carga:
            return self.buscar(chave, raiz.direita)
        else:
            return self.buscar(chave, raiz.esquerda)

    def remover(self, chave, raiz=RAIZ):
        if raiz == RAIZ:
            raiz = self.raiz

        if raiz is None:
            return None

        if chave < raiz.carga:
            raiz.esquerda = self.remover(chave, raiz.esquerda)
        elif chave > raiz.carga:
            raiz.direita = self.remover(chave, raiz.direita)
        else:
            ## Encontramos o elemento
            if raiz.esquerda is None:
                return raiz.direita
            elif raiz.direita is None:
                return raiz.esquerda
            else:
                menor_elemento = self.minimo(raiz.direita)
                raiz.carga = menor_elemento
                raiz.direita = self.remover(menor_elemento, raiz.direita)
        return raiz

    def minimo(self, raiz):
        while raiz.esquerda is not None:
            raiz = raiz.esquerda
        return raiz.carga

    def altura(self, raiz):
        if raiz is None:
            return -1
        return 1 + max(self.altura(raiz.esquerda), self.altura(raiz.direita))

    def count(self, raiz):
        if raiz is None:
            return 0
        return self.count(raiz.esquerda) + self.count(raiz.direita) + 1

    def leafs(self, raiz):
        if raiz is None:
            return 0
        if raiz.esquerda is None and raiz.direita is None:
            return 1
        return self.leafs(raiz.esquerda) + self.leafs(raiz.direita)

    def leafs_elements(self, raiz, leafs=[]):
        if raiz is None:
            return leafs
        if raiz.esquerda is None and raiz.direita is None:
            leafs.append(raiz)
            return leafs
        self.leafs_elements(raiz.esquerda, leafs)
        self.leafs_elements(raiz.direita, leafs)
        return leafs
    def get_level(self, raiz, key, level=0):
        if raiz is None:
            return 0
        if raiz.carga == key:
            return level

        # Procura na subárvore esquerda
        nivel_esquerda = self.get_level(raiz.esquerda, key, level + 1)

        # Se a chave foi encontrada na subárvore esquerda, retorna o nível
        if nivel_esquerda != 0:
            return nivel_esquerda

        # Se a chave não foi encontrada na subárvore esquerda, procura na subárvore direita
        return self.get_level(raiz.direita, key, level + 1)

    def libera(self, raiz, key):
        if raiz is not None:
            raiz.esquerda = self.libera(raiz.esquerda, key)
            raiz.direita = self.libera(raiz.direita, key)
            if raiz.carga == key:
                return None
        return raiz
