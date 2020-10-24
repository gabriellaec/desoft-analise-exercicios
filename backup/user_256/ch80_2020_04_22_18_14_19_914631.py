def interseccao_chaves(d1, d2):
    lista = []
    for chaves in d1.keys():
        if chaves in d2.keys():
            lista.append(chaves)
    return lista
    