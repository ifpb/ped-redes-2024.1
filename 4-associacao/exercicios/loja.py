class Pedido:
    def __init__(self):
        self.__itens_pedido = []

    def obter_total(self):
        return sum([item.produto.valor * item.quantidade for item in self.__itens_pedido])

    @property
    def itens_pedido(self):
        return self.__itens_pedido
    
    def adicionar_item(self, item):
        assert isinstance(item, ItemPedido), 'O item deve ser uma instância de ItemPedido'
        self.__itens_pedido.append(item)
    
    def remover_item(self, item):
        self.__itens_pedido.remove(item)

class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    @property
    def produto(self):
        return self.__produto
    
    @produto.setter
    def produto(self, produto):
        assert isinstance(produto, Produto), 'O produto deve ser uma instância de Produto'
        self.__produto = produto

    @property
    def quantidade(self):
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade):
        assert isinstance(quantidade, int), 'A quantidade deve ser um número inteiro'
        self.__quantidade = quantidade

class Produto:
    def __init__(self, codigo, valor, descricao):
        self.codigo = codigo
        self.valor = valor
        self.descricao = descricao

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, v):
        assert isinstance(v, (int, float)), 'O valor deve ser um número'
        self.__valor = v

if __name__ == '__main__':
    produto = Produto('123', 10.0, 'Produto 1')
    item = ItemPedido(produto, 2)
    pedido = Pedido()
    pedido.adicionar_item(item)
    print(pedido.itens_pedido[0].produto.descricao) # Deve imprimir 'Produto 1'
    print("Total do pedido:", pedido.obter_total()) # Deve imprimir 20.0
    pedido.remover_item(item)
    print(pedido.itens_pedido) # Deve imprimir uma lista vazia