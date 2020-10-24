def inverte_lista(lista):
    i = 0
    while i < (len(lista) - 1):
        lista.insert(i, lista.pop())
        i += 1
    return lista