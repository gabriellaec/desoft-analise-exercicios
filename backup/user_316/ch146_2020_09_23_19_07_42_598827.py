def conta_ocorrencias(l):
    dicionario = {}
    for i in range(len(l)):
        if l[i] not in dicionario:
            dicionario[l[i]] = l.count(l[i])
            
    return dicionario