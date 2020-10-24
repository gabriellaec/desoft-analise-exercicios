def conta_ocorrencias(lista):
    dicionario = {}
    for i in lista:
        if lista[i] not in dicionario:
            dicionario[lista[i]] = 1
        else:
            dicionario[lista[i]] += 1
    return dicionario