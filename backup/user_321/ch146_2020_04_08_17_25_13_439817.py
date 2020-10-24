def conta_ocorrencias(l):
    e = 1
    dicionario = {}
    for i in l:
        if i in dicionario:
            e += 1
            dicionario[i] = e
        else:
            dicionario[i] = e
    return dicionario