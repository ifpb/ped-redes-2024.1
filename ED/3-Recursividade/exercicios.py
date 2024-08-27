def contem_par(lista):
    if len(lista) > 0:
        elemento = lista[0]
        if elemento % 2 == 0:
            return True
        else:
            return contem_par(lista[1:])
    return False

def todos_impares(lista):
    if len(lista) > 0:
        elemento = lista[0]
        if elemento % 2 == 0:
            return False
        else:
            return todos_impares(lista[1:])
    return True

def pos_max(lista, pos=0, i=1):
    if len(lista) == 0:
        return -1
    if i < len(lista):
        if lista[i] > lista[pos]:
            pos = i
        return pos_max(lista, pos, i+1)
    return pos

def inverte_lista(lista, invertida=[]):
    if len(lista) > 0:
        elemento = lista[-1:][0]
        invertida.append(elemento)
        inverte_lista(lista[:-1], invertida)
    return invertida

def lista_igual(lista1, lista2):
    if len(lista1) > 0 or len(lista2) > 0:
        if len(lista1) != len(lista2):
            return False
        elemento1 = lista1[0]
        elemento2 = lista2[0]
        if elemento1 != elemento2:
            return False
        return lista_igual(lista1[1:], lista2[1:])
    return True

lista = [1,3,7,5,3,10]
# print(inverte_lista(lista))

print("Lista igual = ", lista_igual([1,2,3], [1,2,3]))