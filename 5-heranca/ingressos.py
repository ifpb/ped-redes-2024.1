class Ingresso:
    def __init__(self, valor):
        self.valor = valor

    def get_valor(self):
        return self.valor

class IngressoVIP(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional
    
    def get_valor(self):
        return super().get_valor() + self.adicional
    
if __name__ == '__main__':
    ingresso = Ingresso(100)
    print(ingresso.get_valor())
    ingresso_vip = IngressoVIP(100, 50)
    print(ingresso_vip.get_valor())
