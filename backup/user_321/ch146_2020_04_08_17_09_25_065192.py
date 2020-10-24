def conta_ocorrencias(l):
    v = 1
    for i in range(len(l)):
        if l[i] in dicionario:
            dicionario = {l[i]: v+=1}
        else:
            dicionario = {l[i]: 1}
    return dicionario