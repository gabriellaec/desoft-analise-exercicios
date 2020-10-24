def monta_dicionario(k,v):
    d = {}
    for e in range(len(k)-1):
        d[k[e]] = [v[e]]
    return d