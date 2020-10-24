def interseccao_valores (dic1,dic2):
    l1 = []
    for i in dic1.values():
        if i in dic2.values():
            l1.append(i)
    return l1
                   