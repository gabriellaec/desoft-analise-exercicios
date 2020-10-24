def interseccao_chaves(dic1,dic2):
    dict = {}
    for k in dic1:
        if k in dic2:
            dict[k] = dic1[k]
    return dict