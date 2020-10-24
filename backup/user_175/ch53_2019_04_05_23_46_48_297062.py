def inverte_lista(lista):
    x = len(lista)
    nova_lista = []
    i = 0
    while i < x:
        nova_lista.append(lista[x-i-1])
        i += 1
    return nova_lista