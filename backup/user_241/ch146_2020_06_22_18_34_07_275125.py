def conta_ocorrencias(lista):
    dicionario = {}
    for letra in lista:
        i = dicionario.get()
        i += 1
        dicionario[letra] = i
    return dicionario