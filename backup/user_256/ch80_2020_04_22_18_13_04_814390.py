def interseccao_chaves(d1, d2):
    lista = []
    for chaves in d1.key():
        if chaves in d2.key():
            lista.append(chaves)
    return lista
    