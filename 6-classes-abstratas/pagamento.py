from abc import ABC, abstractmethod

class Pagamento(ABC):

    def __init__(self, valor):
        self.valor = valor

    @abstractmethod
    def pagar(self):
        pass

    def coletar_detalhes_pagamento(self):
        return f"O valor a ser pago é: R$ {self.valor}"

class PagamentoCartaoDeCredito(Pagamento):
    def __init__(self, valor, cartao):
        super().__init__(valor)
        self.cartao = cartao
    
    def pagar(self, valor):
        print(f"Pagando R$ {valor:.2f} com cartão de crédito")
        print(f"Cartão: {self.cartao.numero}"
              f"\nValidade: {self.cartao.validade}"
              f"\nCVV: {self.cartao.cvv}"
              f"\nLimite: R$ {self.cartao.limit:.2f}")
        

class PagamentoPix(Pagamento):
    def __init__(self, valor, pix):
        super().__init__(valor)
        self.pix = pix

    def pagar(self, valor):
        print(f"Pagando R$ {valor:.2f} com Pix")
        print(f"Chave: {self.pix.chave}"
              f"\nTipo: {self.pix.tipo}")

class Pedido:
    def __init__(self):
        self.total = 0
        self.fechado = False
    
    def processar_pagamento(self, pagamento):
        pagamento.pagar(self.total)

    def fechar_pedido(self):
        self.fechado = True

class CartaoDeCredito:
    def __init__(self, limite, numero, validade, cvv):
        self.limit = limite
        self.numero = numero
        self.validade = validade
        self.cvv = cvv

class Pix:
    def __init__(self, chave, tipo):
        self.chave = chave
        self.tipo = tipo


if __name__ == '__main__':
    pedido = Pedido()
    pedido.total = 1000
    cartao = CartaoDeCredito(2000, '123123131231231', '12/25', '123')
    pix = Pix('123456789', 'CPF')
    pagamento_cartao = PagamentoCartaoDeCredito(1000, cartao)
    pagamento_cartao.coletar_detalhes_pagamento()
    pagamento_pix = PagamentoPix(2000, pix)
    pagamento_pix.coletar_detalhes_pagamento()
    pedido.processar_pagamento(pagamento_cartao)
    pedido.processar_pagamento(pagamento_pix)
    pedido.fechar_pedido()
    print(pedido.fechado)

