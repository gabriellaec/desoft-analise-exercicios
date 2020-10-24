def conta_ocorrencias(lista):
    dicionario = {}
    for e in lista:
        if e in dicionario:
            dicionario[e] += 1
        else:
            dicionario[e] = 1
    return (dicionario)