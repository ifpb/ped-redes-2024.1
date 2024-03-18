from statistics import mean

class Aluno:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome
        self.__notas = []

    def add_nota(self, nota):
        assert len(self.__notas) <= 5, "O aluno só pode ter no máximo 5 notas"
        self.__notas.append(nota)

    def calcular_media(self):
        assert len(self.__notas) > 0, "Deve existir ao menos uma nota para calcular a média"
        # return sum(self.__notas) / len(self.__notas)
        return mean(self.__notas)

    def __str__(self):
        return f"{self.matricula} - {self.nome}"

    @property
    def notas(self):
        return self.__notas

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, m):
        self.__matricula = m

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, n):
        self.__nome = n

if __name__ == '__main__':
    a = Aluno("202223123", "Maria Hisabel")
    print(a)
    a.add_nota(7)
    a.add_nota(8)
    a.add_nota(9)
    a.add_nota(4)
    try:
        print("Média = ", a.calcular_media())
    except AssertionError as e:
        print(e)
