def eh_crescente(lista):
    n = len(lista)
    i = 1
    while i < n:
        if lista[i-1] < lista[i]:
            i += 1
        else:
            return False
    return True