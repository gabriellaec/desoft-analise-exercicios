def conta_ocorrencias (lista):
    dicionario = {}
    for i in lista:
        if i is not in dicionario:
            dicionario[i] = 1
        else:
            dicionario[i] += 1
    return dicionario
        