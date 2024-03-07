import random

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return f"{self.valor} de {self.naipe}"
    
    def calcular_valor(self):
        if self.valor == 'A':
            return 0
        elif self.valor == 'J':
            return 11
        elif self.valor == 'Q':
            return 12
        elif self.valor == 'K':
            return 13
        else:
            return int(self.valor)
        

class Baralho:
    def __init__(self):
        valores = [str(i) for i in range(2,11)] + list('JQKA')
        naipes = ["espadas", "paus", "ouro", "copas"]
        self.cartas = [Carta(valor, naipe) for valor in valores for naipe in naipes]

    def embaralhar(self):
        random.shuffle(self.cartas)

    def esta_vazio(self):
        return len(self.cartas) == 0

    def retirar_carta(self):
        if len(self.cartas) == 0:
            return None
        else: 
            return self.cartas.pop() 

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.cartas = []
        self.pontuacao = 0

    def adicionar_carta(self, carta):
        self.cartas.append(carta)
        self.calcular_pontuacao()

    def calcular_pontuacao(self):
        self.pontuacao = sum([carta.calcular_valor() for carta in self.cartas])
    
    def mostrar_cartas(self):
        print("Cartas do jogador", self.nome)
        for carta in self.cartas:
            print(carta)

    def __str__(self):
        return f"Nome = {self.nome}, Pontuação = {self.pontuacao}"

class Partida:
    def __init__(self, jogadores):
        assert len(jogadores) > 1 and len(jogadores) <= 4, "Jogo inválido"
        self.jogadores = jogadores
        self.baralho = Baralho()
        self.baralho.embaralhar()

    def distribuir_cartas(self):
        while not self.baralho.esta_vazio():
            for jogador in self.jogadores:
                carta_retirada = self.baralho.retirar_carta()
                if carta_retirada is not None:
                    jogador.adicionar_carta(carta_retirada)

    def imprimir_ranking(self):
        self.jogadores.sort(reverse=True, key=lambda j: j.pontuacao)
        for jogador in self.jogadores:
            print(jogador)
        print(f"Jogador vencedor foi {jogadores[0].nome}!!!")
        pontuacao_vencedora = jogadores[0].pontuacao
        vencedores = [jogadores[0]]
        for i in range(1, len(self.jogadores)):
            if jogadores[i] == pontuacao_vencedora:
                vencedores.append(jogadores[i])

        if len(vencedores) > 1:
            print("Houve empate entre os jogadores: ")
            print(vencedores)
    
jogador1 = Jogador("Rodolpho")
jogador2 = Jogador("William")
jogador3 = Jogador("Diego")
jogadores = [jogador1, jogador2, jogador3]
partida = Partida(jogadores)
partida.distribuir_cartas()
partida.imprimir_ranking()