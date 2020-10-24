def total_do_semestre_por_bairro(dicionario):
  dicionario2={}
  for k in dicionario:
    for i in range(6,12):
      if not k in dicionario2:
        dicionario2[k] = dicionario[k][i]
      else:
        dicionario2[k] += dicionario[k][i]

  return dicionario2


def bairro_mais_custoso(dicionario):
  maior_bairro=0
  nome_bairro=0
  bairros2= total_do_semestre_por_bairro(dicionario)
  for k in bairros2:
    if bairros2[k]>maior_bairro:
      maior_bairro=bairros2[k]
      nome_bairro=k
  return nome_bairro