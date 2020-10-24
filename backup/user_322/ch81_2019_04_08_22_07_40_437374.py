def interseccao_valores(x):
    lista = []
    m = x[0]
    n = x[1]
    for k,v, in m.items():
        for k2,v2, in n.items():
            v = str(v)
            v2 = str(v2)
            if v in v2:
                lista.append(v)
    return lista
    