def inverte_dicionario(d):
    new_d = {}
    for k,v in d.items():
        if not v in new_d:
            new_d[v] = k
        else:
            new_d[v] = k
    return new_d