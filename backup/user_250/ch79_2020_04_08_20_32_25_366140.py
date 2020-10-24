def monta_dicionario(k,v):
    d = {}
    for e in range(0, len(k)):
        d[k[e]] = [v[e]]
    return d