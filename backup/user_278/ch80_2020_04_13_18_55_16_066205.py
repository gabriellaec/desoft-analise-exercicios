def interseccao_chaves (dic1, dic2):
    l1 = []
    for i in dic1:
        if i in dic2:
            l1.append(i)
    return l1