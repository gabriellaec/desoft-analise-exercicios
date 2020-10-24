def inverte_lista (lista):
    i = len(lista) - 1
    e = 0
    aux = 0
    while e < i:
        aux = lista[e]
        lista [e] = lista[i]
        lista [i] = aux
        i -= 1
        e += 1
    return lista

def inverte_lista (lista):
    lista = lista[::-1] #fatiamento
    return lista