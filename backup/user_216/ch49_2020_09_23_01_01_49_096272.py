def inverte_lista(lista):
    nova_lista = []
    i = len(lista) - 1
    while i >= 0:
        nova_lista.append(lista[i])
        i -= 1
    return nova_lista