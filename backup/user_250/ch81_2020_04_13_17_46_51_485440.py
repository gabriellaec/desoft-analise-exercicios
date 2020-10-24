def interseccao_valores(dic1,dic2):
    lista = []
    for k in dic1:
        if dic1[k] in dic2:
            lista.append(dic1[k])
    return lista