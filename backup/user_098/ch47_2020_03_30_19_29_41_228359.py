def estritamente_crescente(lista):
  i=1
  j=0
  somente_crescente=[lista[0]]
  while i<len(lista):
    if int(lista[i])>int(somente_crescente[j]):
      somente_crescente.append(lista[i])
      j+=1
    i+=1
  somente_crescente =  list(dict.fromkeys(sorted(somente_crescente)))
  return somente_crescente