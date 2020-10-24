def conta_ocorrencias (lista):
    i = 0
    dicionario = {}
    while i < len(lista):
        x = 0
        if lista[i] in dicionario:
            x = x + 1
            dicionario[lista[i]] = x
        else:
            dicionario[lista[i]] = 1
        i = i + 1
    return dicionario