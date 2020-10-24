def quantos_uns(numero):
  numero=str(numero)
  i=0
  resultado=0
  while i<len(numero):
    if numero[i]=='1':
      resultado+=1
    i+=1
  return resultado