def conta_ocorrencias(lista):
    dicionario = {}
    i = 0
    if lista[i] not in dicionario:
        dicionario[lista[i]] = 1
        i += 1
    else:
        dicionario[lista[i]] += 1
        i += 1
    return dicionario