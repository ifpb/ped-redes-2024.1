def busca_binaria(chave, vetor) -> int:
  primeiro: int = 0
  ultimo: int = len(vetor)-1
  i = 0

  while primeiro <= ultimo:
    print(f"Passo {i+1}")
    meio = (primeiro + ultimo) // 2
    if vetor[meio].ip == chave:
      ## Item encontrado
      return vetor[meio].nome

    if chave < vetor[meio].ip:
      ultimo = meio - 1
    else:
      primeiro = meio + 1

    i += 1

  return -1 ## item não encontrado

def busca_binaria_recursiva(chave, vetor, primeiro=0, ultimo=None):

  if ultimo is None:
    ultimo = len(vetor)-1

  meio = (primeiro + ultimo) // 2

  if vetor[meio].ip == chave:
    return vetor[meio].nome

  if meio == 0 or primeiro == ultimo:
    return -1

  if chave < vetor[meio].ip:
    return busca_binaria_recursiva(chave, vetor, primeiro, meio-1)
  else:
    return busca_binaria_recursiva(chave, vetor, meio+1, ultimo)