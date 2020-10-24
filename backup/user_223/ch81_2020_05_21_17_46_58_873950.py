def interseccao_valores(d1, d2):
    interseccao=[]
    for i in d1.values():
        if i in d2.values():
            interseccao.append(i)
    return interseccao