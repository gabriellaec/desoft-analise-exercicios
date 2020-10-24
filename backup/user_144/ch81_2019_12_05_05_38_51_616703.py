def interseccao_valores(dic1,dic2):
    lista = []
    for i in dic1:
        for e in dic2:
            if dic[e] == dic[i]:
                lista.append(dic[e])
    return lista