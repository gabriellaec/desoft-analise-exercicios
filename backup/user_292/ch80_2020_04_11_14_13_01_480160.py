def interseccao_chaves(d1,d2):
    d = []
    for i in d1:
        if i in d2:
            d.append(i)
    return d