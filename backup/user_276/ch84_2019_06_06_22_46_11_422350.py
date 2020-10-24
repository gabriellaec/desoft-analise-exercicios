dicinv = {}
lista = []
def inverte_dicionario(dic):
    for k, v in dic.items():
        if v not in dicinv:
            dicinv[v] = k
        elif v in dicinv:
            lista.append(k)
    return dicinv