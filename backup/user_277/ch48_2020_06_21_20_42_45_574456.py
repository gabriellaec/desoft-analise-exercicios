def eh_crescente(lista):
    i = 1
    k = True
    while i < len(lista):
        if lista[i+1] <= lista[i]:
            k = False
            i+=1
    if k:
        return True
    else:
        return False