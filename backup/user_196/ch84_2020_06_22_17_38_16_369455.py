from collections import Counter, defaultdict

def inverte_dicionario(dic):
    dicionario_inv = defaultdict(list)
    for k, v in d.items():
        dicionario_inv[v].append(k)
    return dicionario_inv