def eh_crescente(lista):
    i = 1
    crescente = True
    while i<len(lista):
        if lista[i]<= lista[i-1]:
            crescente = False
        i += 1
    return crescente
            
            
      