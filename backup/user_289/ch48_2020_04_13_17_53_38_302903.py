def eh_crescente(lista): 
    i = 1
    L = len(lista)
    while i < L:
        if lista[i-1] < lista[i]:
            i += 1
        else:
            return False
    return True