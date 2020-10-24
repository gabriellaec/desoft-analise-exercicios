def inverte_dicionario(dicionario):
    novo = {}
    for k, v in dicionario.items():
        if v not in novo:
            novo[v] = [k]
        else:
            novo[v].append(k)
    return novo