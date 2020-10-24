def inverte_lista(lista):
    l = []
    i = 0
    a = 1
    while i < len(lista):
        l.append(lista[len(lista)-a])
        a += 1
        i += 1
    return l