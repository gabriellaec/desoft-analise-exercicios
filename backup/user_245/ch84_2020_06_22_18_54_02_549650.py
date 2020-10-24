def inverte_dicionario(dicio):
    dicio_novo = {}
    for i in dicio:
        idade = dicio[i]
        if idade in dicio_novo:
            di[idade].append(i)
        else:
            dic[idade]=[i]
    return dicio_novo