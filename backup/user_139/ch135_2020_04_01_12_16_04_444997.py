def equaliza_imagem (lista, k):
    i = 0 
    while i < int(len(lista)):
        lista[i] = lista [i] * k
        if lista [i] > 225:
            lista [i] = 225
        i += 1
    return lista