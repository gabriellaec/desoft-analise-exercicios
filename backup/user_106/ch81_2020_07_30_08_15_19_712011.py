def interseccao_valores(dic1, dic2):
    lista = []
    for i in dic1:
        for x in dic2:
            if dic2[x] == dic1[i]:
                lista.append(dic1[i])
    return lista