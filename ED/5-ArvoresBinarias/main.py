from arvore import ArvoreBinariaBusca, No
## Q2
no1 = No(1)
no2 = No(2)
no2.direita = No(4)
no1.esquerda = no2
no3 = No(3)
no3.esquerda = No(5)
no3.direita = No(6)
no1.direita = no3
arvore = ArvoreBinariaBusca(no1)

## Q3
print("Pré-ordem: ", end=" ")
arvore.pre_ordem()
print("\nEm-ordem: ", end=" ")
arvore.em_ordem()
print("\nPós-ordem: ", end=" ")
arvore.pos_ordem()

## Q4
print("\nAltura da árvore = ", arvore.altura(arvore.raiz))

## Q5
print("\nQuantidade de nós da árvore = ", arvore.count(arvore.raiz))

## Q6
print("\nQuantidade de nós folha = ", arvore.leafs(arvore.raiz))
print("Nós folhas = ", [str(e) for e in arvore.leafs_elements(arvore.raiz)])
## Q7
print("\nNível do elemento 3 = ", arvore.get_level(arvore.raiz, 3))
print("Nível do elemento 6 = ", arvore.get_level(arvore.raiz, 6))
print("Nível do elemento 2 = ", arvore.get_level(arvore.raiz, 2))
print("Nível do elemento 1 = ", arvore.get_level(arvore.raiz, 1))

## Q8
arvore.libera(arvore.raiz, 3)
arvore.em_ordem()

