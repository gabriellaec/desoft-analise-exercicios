def inverte_lista(lista):
  lista2=[]
  for i in range(len(lista)-1,-1,-1):
    lista2.append(lista[i])
  return lista2