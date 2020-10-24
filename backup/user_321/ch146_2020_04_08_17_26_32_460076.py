def conta_ocorrencias(l):
    e = 1
    dicionario = {}
    for i in l:
        if i in dicionario:
            dicionario[i] = e+1
        else:
            dicionario[i] = e
    return dicionario