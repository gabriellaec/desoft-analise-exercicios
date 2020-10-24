def eh_crescente(lista):
    i=0
    c=0
    while i < len(lista):
        if i == 0:
            c=lista[i]
        if lista[i] > c:
            c=lista[i]
            i+=1
        else:
            return False
    return True