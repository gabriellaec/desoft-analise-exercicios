def conta_ocorrencias(lista):
    dicionario = {}
    for i in range(0,len(lista)):
        dicionario[lista[i]] = lista.count(lista[i])
    return dicionario