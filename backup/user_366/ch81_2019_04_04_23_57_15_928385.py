def interseccao_valores(dic1, dic2):
    lista = []
    for k, v in dic1.items():
        for c, w in dic2.items():
            if v == w:
                lista.append(v)
    return lista