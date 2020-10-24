def inverte_lista(lista):
    a = len(lista)
    l = []
    b = a - 1
    while b >=0:
        l.append(lista[b])
        b -= 1
    return l