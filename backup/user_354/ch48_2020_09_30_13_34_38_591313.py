def eh_crescente(lista):
    i=0
    while (i<len(lista)):
      if(lista[i+1]<lista[i]):
        return False
      else:
           return True
    i+=1