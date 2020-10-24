def interseccao_valores(d1,d2):
    d3 = []
    for i in d1.values():
        if i in d2.values():
            d3.append(i)
    return d3