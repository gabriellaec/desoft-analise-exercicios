def interseccao_chaves(d1, d2):
    interseccao=[]
    for i in d1.keys():
        if d1 in d2:
            interseccao.append(i)
    return interseccao