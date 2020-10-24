def interseccao_valres(d1, d2):
    l1 = d1.values()
    l2 = d2.values()
    vlr = []
    for i in range(len(l1)):
        if li[i] in l2:
            vlr.append(li[i])
    return vlr