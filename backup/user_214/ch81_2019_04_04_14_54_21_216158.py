def interseccao_valores(dic1, dic2):
    x=[]
    for a in dic1:
        if dic1[a] in dic2:
            x.append(dic1[a])
    return x