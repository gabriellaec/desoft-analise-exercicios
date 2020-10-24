def monta_dicionario(keys, values):
    dicionario = {}
    u = 0
    for i in keys:
        dicionario[i] = values[u]
        u += 1
    return dicionario