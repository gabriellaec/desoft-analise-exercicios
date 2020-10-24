def inverte_dicionario(dicio):
    dicio_novo = {}
    for i in dicio:
        idade = dicio[i]
        if idade in dicio_novo:
            dicio_novo[idade].append(i)
        else:
            dicio_novo[idade]=[i]
    return dicio_novo