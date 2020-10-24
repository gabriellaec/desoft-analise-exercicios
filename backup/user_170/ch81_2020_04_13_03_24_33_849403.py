def interseccao_chaves(dic1, dic2):
    interseccao = []
    for i in dic1.values():
        if i in dic2.values():
            interseccao.append(i)
    return interseccao