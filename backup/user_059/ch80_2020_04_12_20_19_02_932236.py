def interseccao_chaves(d1, d2):
    l = list(d1.keys()) 
    l2 = list(d2.keys())
    k = l+l2
    j = []
    for i in range(len(k)):
        if k[i] not in j:
            j.append(k[i])
    return j