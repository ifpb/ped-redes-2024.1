class Ocultacao:
    def __init__(self):
        self.var = 111
    def setmethod(self, valor):
        self.var = valor
        
obj = Ocultacao()
obj.setmethod(222)
print(obj.var)