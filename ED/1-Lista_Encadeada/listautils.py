from listaencadeada import ListaEncadeada


class ListUtils:

    @staticmethod
    def clonar(lista):
        clone = ListaEncadeada()
        atual = lista.cabeca
        while atual is not None:
            clone.inserir_no_final(atual.carga)
            atual = atual.prox
        return clone

    @staticmethod
    def inverter(lista):
        atual = lista.cabeca
        anterior = None
        while atual is not None:
            prox = atual.prox
            atual.prox = anterior
            anterior = atual
            atual = prox
        lista.cabeca = anterior
        return lista

    @staticmethod
    def join(lista, sep):
        atual = lista.cabeca
        retorno = ""
        while atual is not None:
            retorno += str(atual.carga) + (sep if atual.prox is not None else "")
            atual = atual.prox
        return retorno

    @staticmethod
    # "2,0,3,8,2,0,3"
    def split(palavra, sep):
        lista = ListaEncadeada()
        novo = ""
        i = 0
        for c in list(palavra):
            novo += c if c is not sep else ""
            if c == sep or i == len(list(palavra)) - 1:
                lista.inserir_no_final(novo)
                novo = ""
            i += 1
        return lista

    @staticmethod
    def intercalar(lista1, lista2):
        atual = lista1.cabeca
        atual2 = lista2.cabeca
        lista3 = ListaEncadeada()
        while atual is not None or atual2 is not None:
            if atual is not None:
                lista3.inserir_no_final(atual.carga)
                atual = atual.prox

            if atual2 is not None:
                lista3.inserir_no_final(atual2.carga)
                atual2 = atual2.prox

        return lista3
