def interseccao_chaves(d1,d2):
    lista = []
    for i in d1:
        for t in d2:
            if t == i:
                lista.append(t)
    return lista