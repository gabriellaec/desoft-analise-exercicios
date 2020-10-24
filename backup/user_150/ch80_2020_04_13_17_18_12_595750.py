def interseccao_chaves(dic1, dic2):
    lista = []
    for k in dic1.keys():
        if dic2[k]:
            lista.append(k)
    return lista