def interseccao_valores(d1,d2):
    d = []
    for i in d1.values():
        if i in d2.values():
            d.append(i)
    return d