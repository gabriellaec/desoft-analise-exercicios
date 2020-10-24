def interseccao_valores(d1,d2):
    lista = []
    for c in d1.values():
        if c in d2.values():
            lista.append(c)
    return lista