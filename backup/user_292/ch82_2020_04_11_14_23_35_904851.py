def primeiras_ocorrencias(pala):
    d = {}
    for i in range(len(pala)):
        if pala[i] not in d:
            d[pala[i]] = i
    return d