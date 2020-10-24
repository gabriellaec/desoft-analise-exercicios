def monta_dicionario(k,v):
    i = 0
    d = {}
    while i < len(k):
        d[k[i]] = v[i]
        i = i+1
    return d