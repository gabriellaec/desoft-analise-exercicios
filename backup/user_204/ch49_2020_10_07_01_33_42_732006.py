def inverte_lista(lista):
    i = 0
    while i <= len(lista):
        lista.append(lista[i])
        del(lista[i])
        return lista
        i += 1