# marca, modelo, data de fabricação, capacidade do HD, 
# número de série, jogos instalados, anos de garantia

from datetime import datetime

class Videogame:

    __NUM_SERIE_ATUAL = 1

    def __init__(self, data=datetime.now(), marca="", modelo=""):
        self.data = data
        self.marca = marca
        self.modelo = modelo
        self.capacidade_hd = 64
        self.__numero_serie = self.__get_prox_num_serie()
        self.__jogos_instalados = []
        self.anos_garantia = 5

    def __del__(self):
        print("Objeto com marca",self.marca,"foi destruída")

    @classmethod
    def get_numeros_serie_atual(cls):
        return cls.__NUM_SERIE_ATUAL
    
    @staticmethod
    def converter_data_para_string(data):
        return data.strftime("%d/%m%/Y", data)

    def __get_prox_num_serie(self):
        num_serie = Videogame.__NUM_SERIE_ATUAL
        Videogame.__NUM_SERIE_ATUAL += 1
        return num_serie
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        assert type(data) == datetime, "Data deve ser do tipo datetime"
        self.__data = data

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        assert type(marca) == str, "Marca deve ser um string"
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo):
        assert type(modelo) == str, "Modelo deve ser um string"
        self.__modelo = modelo

    @property
    def capacidade_hd(self):
        return self.__capacidade_hd
    
    @capacidade_hd.setter
    def capacidade_hd(self, capacidade):
        assert type(capacidade) == int, "Capacidade do HD deve ser inteiro"
        self.__capacidade_hd = capacidade

    @property
    def numero_serie(self):
        return self.__numero_serie
    
    @property
    def jogos_instalados(self):
        return self.__jogos_instalados
    
    @property
    def anos_garantia(self):
        return self.__anos_garantia
    
    @anos_garantia.setter
    def anos_garantia(self, anos_garantia):
        assert type(anos_garantia) == int, "Anos de garantia deve ser inteiro"
        self.__anos_garantia = anos_garantia

    def instalar_jogo(self, jogo):
        self.jogos_instalados.append(jogo)

    def __str__(self):
        return f"Data = {self.data}, Marca = {self.marca}, Modelo = {self.modelo}"

v1 = Videogame()
v1.instalar_jogo("Jogo")
v1.instalar_jogo("Jogo", 12312)
v1.marca = "Sony"
v1.modelo = "Playstation 5"
v1.data = datetime.now()
print(v1.modelo)
print("V1=",v1)
v2 = Videogame(datetime.now())
print("V2=",v2)
v3 = Videogame(datetime.now(), "Nintendo", "Switch")
print("V3=",v3)

v4 = Videogame(datetime.now(), "Nintendo")


v3.anos_garantia = 10
v3.jogos_instalados.append("Counter Strike")
print("Anos de garantia = ",v3.anos_garantia)
print("Jogos instalados =", v3.jogos_instalados)
print("Numero de serie de V3", v3.numero_serie)
print(hasattr(v3, 'anos_garantia'))

Videogame.get_numeros_serie_atual()
Videogame.converter_data_para_string(datetime.now())