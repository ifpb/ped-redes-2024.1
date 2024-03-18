class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, d):
        assert type(d) == int, "O dia deve ser um inteiro"
        assert 0 < d <= 31, "O dia deve ser um número entre 1 e 31"
        self.__dia = d

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, m):
        assert type(m) == int, "O mês deve ser um inteiro"
        assert 1 <= m <= 12, "O mês deve ser um número entre 1 e 12"
        self.__mes = m

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, a):
        assert type(a) == int, "O ano deve ser um inteiro"
        assert 1900 <= a <= 2050, "O ano deve ser um número entre 1900 e 2050"
        self.__ano = a

if __name__ == '__main__':
    try:
        dia = int(input("Digite o dia: "))
        mes = int(input("Digite o mês: "))
        ano = int(input("Digite o ano: "))
        d = Data(dia, mes, ano)
        print(d)
    except AssertionError as e:
        print(e)