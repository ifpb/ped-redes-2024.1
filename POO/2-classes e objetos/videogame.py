# marca, modelo, data de fabricação, capacidade do HD, 
# número de série, jogos instalados, anos de garantia

class Videogame:

    num_serie_atual = 1

    def __init__(self, data=None, marca=None, modelo=None):
        self.data = data
        self.marca = marca
        self.modelo = modelo
        self.capacidade_hd = 64
        self.numero_serie = self.get_prox_num_serie()
        self.jogos_instalados = []
        self.anos_garantia = 5

    def get_prox_num_serie(self):
        num_serie = Videogame.num_serie_atual
        Videogame.num_serie_atual += 1
        return num_serie

    def __str__(self):
        return f"Data = {self.data}, Marca = {self.marca}, Modelo = {self.modelo}"
