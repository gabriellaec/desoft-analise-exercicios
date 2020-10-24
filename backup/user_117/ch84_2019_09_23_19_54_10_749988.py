def inverte_dicionario(d1):
    d2 = {}
    for k, v in d1.items():
        if v not in d2:
        	d2[v] = []
        d2[v].append(k)
    return d2