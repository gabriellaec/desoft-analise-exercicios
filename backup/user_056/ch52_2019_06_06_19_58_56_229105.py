def eh_crescente(lista):
    i=0
    while i<len(lista):
        if lista[i]<lista[i]:
            return False
    return True
  
        