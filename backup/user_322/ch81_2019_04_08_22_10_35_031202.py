def interseccao_valores(m,n):
    lista = []
    for k,v, in m.items():
        for k2,v2, in n.items():
            if v == v2:
                lista.append(v)
    return lista
    