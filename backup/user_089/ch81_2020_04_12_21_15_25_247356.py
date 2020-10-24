def interseccao_valores(d1,d2):
    v1 = d1.values()
    lista = []
    for e in v1:
        if e in d2.values():
            lista.append(e)
    return lista