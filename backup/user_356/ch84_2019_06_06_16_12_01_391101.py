def inverte_dicionario(dicio):
    dicio_novo={}
    for k, v in dicio.items():
        if v not in dicio_novo:
            dicio_novo[v]=[k]
        if v in dicio_novo:
            dicio_novo[v].append(k)
    return dicio_novo