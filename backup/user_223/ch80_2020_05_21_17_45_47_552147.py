def interseccao_chaves(d1, d2):
    interseccao=[]
    for i in d1.keys():
        if i in d2.keys():
            interseccao.append(i)
    return interseccao