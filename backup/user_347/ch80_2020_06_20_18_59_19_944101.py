def interseccao_chaves(dic1, dic2):
    lista = []
    for i in dic1:
        for e in dic2:
            if i in dic2:
                lista.append(dic1[i])
    return lista
    