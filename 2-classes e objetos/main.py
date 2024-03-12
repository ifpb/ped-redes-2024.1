from datetime import datetime
from videogame import Videogame

v1 = Videogame()
v1.marca = "Sony"
v1.modelo = "Playstation 5"
v1.data = datetime.now()
print("V1=",v1)
v2 = Videogame(datetime.now())
print("V2=",v2)
v3 = Videogame(datetime.now(), "Nintendo", "Switch")
print("V3=",v3)

v3.anos_garantia = 10
v3.jogos_instalados.append("Counter Strike")
print("Anos de garantia = ",v3.anos_garantia)
print("Jogos instalados =", v3.jogos_instalados)
print("Numero de serie de V3", v3.numero_serie)
print(hasattr(v3, 'anos_garantia'))

print(Videogame.__module__)


