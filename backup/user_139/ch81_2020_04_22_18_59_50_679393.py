def interseccao_valores (x, y):
    lista = []
    for v in x.values():
        if v in y.values():
            lista.append(v)
    return lista