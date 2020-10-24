def interseccao_valores(d1, d2):
    same = list()
    for a in d1.values():
        if a in d2.values():
            same.append(a)
    return same