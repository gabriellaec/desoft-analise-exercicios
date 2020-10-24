def interseccao_chaves(d1, d2):
    same = list()
    for a in d1.keys():
        if a in d2.keys():
            same.append(a)
    return same