def eh_crescente(lista):
    for e in range(0,len(lista)-1):
        if lista[e+1]<lista[e]:
            return False
    return True
  
        