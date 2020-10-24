def conta_ocorrencias(l):
    e = 1
    dicionario = {}
    for i in l:
        dicionario[i] = e
        if i in dicionario:
            e += 1
            
    return dicionario