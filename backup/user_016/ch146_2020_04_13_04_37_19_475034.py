def conta_ocorrencias(lista):
    for i in lista:
        dicionario[lista[i]] = lista.count(lista[i])
    return dicionario