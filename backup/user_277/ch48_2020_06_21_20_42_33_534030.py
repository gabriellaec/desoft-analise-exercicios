def eh_crescente(lista):
    i = 1
    k = True
    while i < len(lista):
        if lista[i+1] <= lista[i]:
            k = False
    if k:
        return True
    else:
        return False