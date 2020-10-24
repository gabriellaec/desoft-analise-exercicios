def faixa_notas(lista):
  n1=0
  n2=0
  n3=0
  for contadori in lista:
    if contadori>7:
      n3+=1
    elif contadori<5:
      n1+=1
    else:
      n2+=1
  notas=[n1,n2,n3] 
  return notas

