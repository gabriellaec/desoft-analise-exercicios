def interseccao_chaves(dic1, dic2):
    lista = []
    for i in dic1:
        for x in dic2:
            if x == i:
                lista.append(i)
    return lista