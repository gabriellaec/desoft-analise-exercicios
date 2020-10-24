def primeiras_ocorrencias(palavra):
    d = {}
    for e in palavra:
        if e not in d:
            d[e] = e            
    return d