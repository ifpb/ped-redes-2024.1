class Visor:
    def __init__(self):
        self.preço  = 0.0
        self.litros = 0.0
        self.total  = 0.0
    
    def zerar(self):
        self.litros = 0.0
        self.total  = 0.0

    def exibir(self):
        print( self.__str__())
    
    def set_visor(self, preço:float, litros:float, total:float):
        self.preço  = preço
        self.litros = litros
        self.total  = total
    
    def __str__(self)->str:
        return f'Preço: {self.preço:.2f} | Litros: {self.litros:.1f} | Total: {self.total:.2f}'


