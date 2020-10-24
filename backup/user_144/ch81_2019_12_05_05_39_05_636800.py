def interseccao_valores(dic1,dic2):
    lista = []
    for i in dic1:
        for e in dic2:
            if dic2[e] == dic1[i]:
                lista.append(dic2[e])
    return lista