def interseccao_valores(d1,d2):
    lista = []
    c = 0
    for c in d1:
        if c in d2:
            lista.append(c)
    return lista