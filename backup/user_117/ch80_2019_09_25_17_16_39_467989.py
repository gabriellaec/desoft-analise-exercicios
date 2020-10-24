def interseccao_chaves(d1,d2):
    lista = []
    for k in d1.keys():
        if k in d2:
            lista.append(k)
    return lista