def conta_ocorrencias(l):
    v = 1
    dicionario = {}
    for i in range(len(l)):
        if l[i] in dicionario.keys:
            v += 1
            dicionario = {l[i]: v}
        else:
            dicionario = {l[i]: 1}
    return dicionario