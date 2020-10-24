def eh_crescente(lista):
    i=0
    c=0
    while i < len(lista):
        if i == 0:
            c=lista[i]
            i+=1
            continue
        if lista[i] > c:
            c=lista[i]
        else:
            return False
        i+=1
    return True