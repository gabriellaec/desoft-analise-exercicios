def conta_ocorrencias(lista):
    dicionario = {}
    for i in lista:
        x = lista.count(lista)
        x += 1
        dicionario[i] = x
    return dicionario