def conta_ocorrencias (lista):
    lista =[]
    dicionario = {}
    n = str
    for n in dicionario:
        if not n in lista:
            lista[n] = '1'
        else:
            lista[n] += '1'
    return dicionario
