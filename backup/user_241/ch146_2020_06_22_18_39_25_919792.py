def conta_ocorrencias(lista):
    dicionario = {}
    for i in lista:
        x = lista.count(lista)
        dicionario[x] = i
    return dicionario