def inverte_dicionario(dicio):
    dicionew = dict()
    i = 0
    while i <= (len(dicio)-1):
        dicio[i] = i
        i += 1
    return dicionew