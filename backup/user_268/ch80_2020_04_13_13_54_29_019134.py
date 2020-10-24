def interseccao_chaves(d1, d2):
    c1 = d1.keys()
    c2 = d2.keys()
    lista = []
    for c1 in c2:
        if c1 not in lista:
            lista.append(c1)
    return lista
        