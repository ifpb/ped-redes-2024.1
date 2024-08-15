from visor import Visor
from combustivel import Combustivel
from bomba_de_combustivel import BombaDeCombustivel


v1 = Visor()
print(id(v1))

preço = 5.57
litros = 0
total = 0

v1.set_visor(preço, litros, total)
v1.exibir()

v1.zerar()

for i in range(1, 11):
    v1.set_visor(preço, i, preço * i)
    #v1.exibir()
    print(v1)
#print(v2.__dict__)
print()
print(v1)

b1 = BombaDeCombustivel(Combustivel.GASOLINA, Combustivel.ALCOOL)
b2 = BombaDeCombustivel(Combustivel.ALCOOL, Combustivel.DIESEL)
b3 = BombaDeCombustivel(Combustivel.DIESEL, Combustivel.GASOLINA)
b4 = BombaDeCombustivel(Combustivel.GNV, Combustivel.GASOLINA)
print(b1)
print(b2)
print(b3)
b1.alterar_preço(Combustivel.GASOLINA, 5.00)
b1.alterar_preço(Combustivel.ALCOOL, 4.29)
# b1.alterar_preço(Combustivel.DIESEL, 5.70)
print(b1)
b1.preparar_abastecimento(Combustivel.GASOLINA)
b1.abastecer_por_valor(Combustivel.GASOLINA, 23.00) 
