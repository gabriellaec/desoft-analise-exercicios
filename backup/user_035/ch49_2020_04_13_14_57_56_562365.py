def inverte_lista(lista):
    l = []
    a = 0
    i = 0
    while a < len(lista)-1:
        l.append(lista[len(lista)-i])
        a += 1
        i += 1
    return l