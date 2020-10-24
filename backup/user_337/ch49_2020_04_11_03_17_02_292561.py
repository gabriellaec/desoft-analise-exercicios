'''def inverte_lista(lista):
    list2 = lista[::-1]
    return list2'''

def inverte_lista(lista):
    inv = []
    x = len(lista) -1
    while x >= 0:
        inv.append(lista[x])
        x = x - 1
    return inv