def eh_crescente(lista):
    i=0
    while i < len(lista):
        sub = lista[i+1] - lista[i]
        if sub < 0:
            return False
        i +=1
    return True
