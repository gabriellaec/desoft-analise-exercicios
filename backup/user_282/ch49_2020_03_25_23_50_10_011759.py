def inverte_lista(lista):
    inv = []
    i = len(lista)-1
    while i>=0:
        inv.append(lista[i])
        i -= 1
    return inv