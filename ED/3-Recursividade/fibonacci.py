def fib_rec(n: int) -> int:
    print(f"Calculando fib({n})")
    if n <= 1:
        return n
    return fib_rec(n-1) + fib_rec(n-2)

def fib_ite(n: int) -> int:
  i: int = 1
  fib: int = 1
  anterior: int = 0
  while i < n:
    temp = fib
    fib = fib + anterior
    anterior = temp
    i += 1
  return fib

# print(fib_ite(5000))

print(fib_rec(50))