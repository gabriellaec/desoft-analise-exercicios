def primeiras_ocorrencias(palavra):
    d = {}
    for e in range(len(palavra)-1):
        if palavra[e] not in d:
            d[palavra[e]] = e            
    return d