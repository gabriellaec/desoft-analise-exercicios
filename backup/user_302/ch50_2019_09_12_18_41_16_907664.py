def numero_no_indice(lista):
  lista = [0, 1, 1, 2, 4]
  lista_fim = []
  i = 0
  while i < len(lista):
    if i == lista[i]:
      lista_fim.append(i)
    i += 1
  return lista_fim