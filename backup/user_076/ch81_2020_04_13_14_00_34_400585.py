def interseccao_valores (d1,d2):
    interseccao = []
    for i in d1:
        if d1[i] in d2:
            interseccao.append(d1[i])
    return interseccao