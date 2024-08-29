def busca_sequencial(chave_pesquisa, vetor):
  for i in range(len(vetor)):
    if vetor[i].ip == chave_pesquisa:
      return vetor[i].nome
    if vetor[i].ip > chave_pesquisa:
      return -1
  return -1

def busca_sequencial_recursiva(chave, vetor, i: int = 0):
  if i >= len(vetor) or vetor[i].ip > chave:
    return -1
  if vetor[i].ip == chave:
    return vetor[i].nome
  return busca_sequencial_recursiva(chave, vetor, i+1)