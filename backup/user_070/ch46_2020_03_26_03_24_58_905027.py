def numero_do_indice(lista):
    x = len(lista)
    i = 0
    while i < x:
        if lista[i] == i:
            i += 1
        else:
            del lista[i]
            i += 1
    return lista