def eh_crescente(lista):
    i=0
    while i<len(lista):
        if lista[i]<lista[i+1]:
            return False
    return True
  
        