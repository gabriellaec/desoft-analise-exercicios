def interseccao_valores(d1,d2):
    d3 = []
    for i,e in d1.items():
        if e in d2:
            d3.append(e)
    return d3