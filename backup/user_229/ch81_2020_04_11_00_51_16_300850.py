def interseccao_valores(dic1, dic2):
    lista = []
    for i in dic1.values():
        if i in dic2.values():
            lista.append(i)
    return lista