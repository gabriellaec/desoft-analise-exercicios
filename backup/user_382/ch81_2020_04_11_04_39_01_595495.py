def interseccao_valores(d1,d2):
    v1 = list(d1.values())
    v2 = list(d2.values())
    lista = []
    for i in v1:
        for t in v2:
            if i == t:
                lista.append(t)
    return lista
