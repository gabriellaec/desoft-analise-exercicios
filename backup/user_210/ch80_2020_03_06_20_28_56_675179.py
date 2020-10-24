def interseccao_chaves(dic1, dic2):
    lista = []
    for c in dic1:
        lista.append(dic1[c])

    for c in dic2:
        lista.append(dic2[c])
    return lista