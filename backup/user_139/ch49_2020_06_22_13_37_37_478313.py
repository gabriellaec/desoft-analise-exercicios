def inverte_lista (lista):
    i = len(lista)
    nova_lista = []
    while i > -1:
        nova_lista.append(lista[i])
        i -= 1
    return nova_lista