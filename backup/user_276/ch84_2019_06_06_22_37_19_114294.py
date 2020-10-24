dicinv = {}
def inverte_dicionario(dic):
    for k, v in dic.items():
        if v not in dicinv:
            dicinv[v] = k
        elif v in dicinv:
            dicinv[v] = k
    return dicinv