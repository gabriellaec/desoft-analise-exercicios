def bairro_mais_custoso(dicionario):
  dicionario2={}
  for k in dicionario:
    for i in range(6,12):
      if not k in dicionario2:
        dicionario2[k] = dicionario[k][i]
      else:
        dicionario2[k] += dicionario[k][i]
   for i in

  return dicionario2