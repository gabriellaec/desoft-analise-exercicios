def eh_crescente(lista):
    i=1
    while i < len(lista):
        sub = lista[1] - lista[i-1]
        if sub < 0:
            return False
        i +=1
    return True
