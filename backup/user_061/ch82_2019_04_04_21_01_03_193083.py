def primeiras_ocorrencias(string):
    dicionario = {}
    for letra in range(len(string)):
        if string[letra] not in dicionario:
            dicionario[string[letra]] = letra
    return dicionario
        