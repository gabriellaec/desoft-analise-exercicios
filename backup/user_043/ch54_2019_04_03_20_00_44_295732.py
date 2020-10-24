def junta_nome_sobrenome(nome,sobrenome):
  i=0
  listacompl=[]
  while i<len(nome):
    completo=nome[i]+' '+sobrenome[i]
    listacompl.append(completo)
    i+=1
  return listacompl
