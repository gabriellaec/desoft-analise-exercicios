def inverte_lista(lista):
    i = 0
    inicio = len(lista)
    while i <= inicio:
        lista.append(lista[i])
        i += 1
    del(lista[inicio])
    return lista