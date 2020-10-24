def inverte_lista(lista):
    i = len(lista) - 1
    nova = []
    while i >= 0 :
        nova.append(lista[i])
        i -= 1
    return nova