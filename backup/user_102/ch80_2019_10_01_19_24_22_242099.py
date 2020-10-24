def interseccao_chaves(q):
    lista3 = []
    for i in q:
        for x in i:
            lista3.append(i[x])
    return q