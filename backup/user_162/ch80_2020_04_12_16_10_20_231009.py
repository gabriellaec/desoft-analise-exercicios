def interseccao_chaves(D1, D2):
    lista = []
    for i in D1:
        for j in i:
            lista.append(j)
    for i in D2:
        for j in i:
            lista.append(j)
    return lista