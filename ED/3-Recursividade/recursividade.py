def imprimir_numero_recursivo(num: int):
  if num < 5:
    print(num)
    imprimir_numero_recursivo(num + 1)

imprimir_numero_recursivo(0)

def soma(m: int, n: int) -> int:
  if m == n:
    return m
  else:
    return m+soma(m+1, n)
  
print(soma(1,5))