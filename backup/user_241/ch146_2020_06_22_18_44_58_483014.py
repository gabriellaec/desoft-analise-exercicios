def conta_ocorrencias(lista):
    for i in lista:
        x = lista.count(i)
        dicionario[i] = x
    return dicionario