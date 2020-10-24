def conta_ocorrencias (lista):
    dicionario = {}
    n = str
    for n in lista:
        if not n in dicionario:
            dicionario[n] = '1'
        else:
            dicionario[n] += '1'
    return dicionario
