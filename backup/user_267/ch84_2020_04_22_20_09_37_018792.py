def inverte_dicionario(dicio):
    dicionew = dict()
    for i in dicio:
        a = dicio[i]
        if a in dicionew:
            dicionew[a] += a[i]
        else:
            dicionew[a] = a
    return dicionew
