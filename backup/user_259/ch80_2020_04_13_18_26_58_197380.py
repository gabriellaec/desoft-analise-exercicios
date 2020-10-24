def interseccao_chaves(dic1, dic2):
    comuns = []
    for i in dic1:
        if i in dic2:
            comuns.append(i)
    return comuns
            