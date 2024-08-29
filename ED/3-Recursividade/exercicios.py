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


'''
Q6
'''
def fatorial(n):
    if n == 1:
        return 1
    return n * fatorial(n - 1)

'''
Q7
'''
def soma_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])

'''
Q8
'''
def potencia(base, expoente):
    if expoente == 0:
        return 1
    return base * potencia(base, expoente-1)

'''
Q9
'''
def contagem_regressiva(n):
    if n == 0:
        print("Fogo!")
    else:
        print(n)
        contagem_regressiva(n-1)

'''
Q10
'''
def inverte_string(s):
    if len(s) == 0:
        return s
    else:
        return inverte_string(s[1:]) + s[0]
    

print("pos max")
print(max([1, 2, 3, 4, 100, 1, 2]))
print(pos_max([1, 2, 3, 4, 100, 1, 2]))

print("Contem par")
lista_pares = [1, 2, 3, 4, 5, 6, 10]
print(contem_par(lista_pares))
print("lista pares")
print(lista_pares)
print("Todos ímpares")
lista = [1, 2, 3, 4, 5, 6, 10]
print(todos_impares(lista))
print("lista impares")
lista_impares = [1, 1, 3, 7, 9, 11, 13]
print(todos_impares(lista_impares.copy()))
print(lista_impares)
print("inverte lista")
lista = [1, 2, 3, 4, 5, 6]
print(inverte_lista(lista))
print("Comparar listas iguais")
print("Listas iguais = ", lista_igual([1, 2, 3], [1, 2, 3]))
print("Fatorial")
print("fatorial de 5 =", fatorial(5))
print("Soma lista")
print(soma_lista([2,3,4,5,7,8,10]))
print("Potência")
print(potencia(4, 2))
print("Contagem regressiva")
print(contagem_regressiva(4))
print("Inverter string")
print(inverte_string("teste"))
