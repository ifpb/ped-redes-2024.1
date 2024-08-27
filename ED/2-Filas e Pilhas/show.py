from fila import Fila


class FilaCheiaException(Exception):
    pass


class FilaShow(Fila):
    def __init__(self, capacidade):
        super().__init__()
        self.capacidade = capacidade
        self.usuarios_aguardando = 0

    def add(self, valor):
        if self.usuarios_aguardando < self.capacidade:
            super().add(valor)
            self.usuarios_aguardando += 1
        else:
            raise FilaCheiaException()

    def remove(self):
        elemento_removido = super().remove()
        self.usuarios_aguardando -= 1
        return elemento_removido


if __name__ == '__main__':
    try:
        fila = FilaShow(4)
        fila.add("Rodolpho")
        fila.add("Daniel")
        fila.add("Lucas")
        fila.add("Ramon")
        print(fila)
        print(fila.remove())
        fila.add("William")
        print(fila)
    except FilaCheiaException:
        print("Fila cheia, não é possível adicionar mais")
