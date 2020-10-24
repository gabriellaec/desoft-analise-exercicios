def eh_crescente(lista):
    i=1
    while i < len(lista):
        if (lista[i] - lista[i-1]) > 0:
            return True
        i +=1
    return False
