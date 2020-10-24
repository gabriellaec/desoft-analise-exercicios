def conta_ocorrencias(l):
    for i in range(len(l)):
        if l[i] in dicionario:
            dicionario = {l[i]: +=1}
        else:
            dicionario = {l[i]: 1}
    return dicionario