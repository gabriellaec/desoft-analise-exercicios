def inverte_lista(lista):
    lista = []
    i = 0
    while i < len(lista):
        del lista[i]
        lista.append(lista[i])
        i += 1