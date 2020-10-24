def interseccao_chaves(dic1, dic2):
    lista = []
    for i in dic1:
        for e in dic2:
            if dic1[i] == dic2[e]:
                lista.append(dic1[1])
    return lista
    