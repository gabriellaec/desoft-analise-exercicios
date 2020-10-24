def interseccao_valores(dic1, dic2):
    lista = []
    for v in dic1.values():
        for vv in dic2.values():
            if v == vv:
                dic1[v].append(lista)
    return lista
    