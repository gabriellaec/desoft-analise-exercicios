def medias_por_inicial(d):
    med = {}
    i = 0
    for n,m in d.items():
        if not n[0] in med:
            med[n[0]]= m
        else:
            med[n[0]] += m
            i += 1
    for c,v in med.items():
        med[c] = v/i
    return med
    