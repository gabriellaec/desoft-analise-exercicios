def inverte_dicionario(dicio):
    dicionew = dict()
    i = 0
    while i <= (len(dicio)-1):
        a = dicio[i]
        dicionew[i] = a
        i += 1
    return dicionew