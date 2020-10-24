def eh_crescente(lista):
    i = len(lista)
    while i > 0:
        a = lista[i-1] > lista[i-2]
        if a = True:
            i -= 1
        else:
            return False
    return True       