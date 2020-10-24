def interseccao_valores(d1, d2):
    l1 = d1.values()
    l2 = d2.values()
    vlr = []
    for i in l1:
        if i in l2:
            vlr.append(i)
    return vlr