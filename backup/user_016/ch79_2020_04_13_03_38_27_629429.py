def monta_dicionario(keys, values):
    dicionario = {}
    for i in keys:
        for u in values:
            dicionario[i] = values[u]
    return dicionario