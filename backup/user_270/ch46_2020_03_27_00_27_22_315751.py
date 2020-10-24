def numero_no_indice(list):
    i = 0
    while i < len(lista):
        if lista[i] != i:
            del lista[i]
        i += 1
    return lista