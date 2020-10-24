def inverte_dicionario(a):
    c = {}
    for k,v in a.items():
        if v not in c:
            c[v] = [k]
        else:
            c[v].append(k)

    return c