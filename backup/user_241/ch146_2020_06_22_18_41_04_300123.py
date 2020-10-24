def conta_ocorrencias(lista):
    dicionario = {}
    for i in lista:
        x = lista.count('')
        dicionario[i] = x
    return dicionario