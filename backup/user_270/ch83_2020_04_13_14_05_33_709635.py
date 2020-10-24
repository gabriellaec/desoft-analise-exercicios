def medias_por_inicial(d):
    med = {}
    med_count = {}
    for i in d:
        if i[0] not in med:
            med[i[0]] = d[i]
            med_count[i[0]] = 1
        else:
            med[i[0]] += d[i]
            med_count[i[0]] += 1
    for k,v in med.items():
        med[k] = v/med_count[k]
    return med
    