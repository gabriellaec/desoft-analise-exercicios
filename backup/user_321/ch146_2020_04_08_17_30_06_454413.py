def conta_ocorrencias(l):
    dicionario = {}
    for i in l:
        if i in dicionario:
            dicionario[i] += 1
        else:
            dicionario[i] = 1
    return dicionario