def interseccao_valores(dic1, dic2):
    comuns = []
    for i in dic1.values():
        if i in dic2.values():
            comuns.append(i)
    return comuns