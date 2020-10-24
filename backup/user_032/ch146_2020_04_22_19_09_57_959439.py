def conta_ocorrencias(lista):
    dicionario = {}
    k = dicionario.keys()
    for i in range (0, len(lista)):
        if lista[i] not in k:
            contador = palavras.count(lista[i])
            dicionario[lista[i]]=contador
    return dicionario