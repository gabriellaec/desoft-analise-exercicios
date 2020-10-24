def conta_ocorrencias(lista):
    dicionario = {}
    for letra in lista:
        i = dicionario.keys()
        dicionario[letra] = i
    return dicionario