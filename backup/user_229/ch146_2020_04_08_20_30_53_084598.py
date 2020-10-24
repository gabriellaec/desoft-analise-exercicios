def conta_ocorrencias(lista):
    dicionario = dict()
    for i in lista:
        if i in dicionario:
            dicionario[i] += 1
        else:
            dicionario[i] = 1
    return dicionario