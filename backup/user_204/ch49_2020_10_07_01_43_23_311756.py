def inverte_lista(lista):
    i = 0
    inicio = len(lista)
    while i < inicio:
        lista.append(lista[i])
        i += 1
    i = 0
    while i < inicio:
        del(lista[i])
        i += 1
    return lista