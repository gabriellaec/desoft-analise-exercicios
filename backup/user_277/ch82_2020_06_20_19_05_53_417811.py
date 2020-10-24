def primeiras_ocorrencias(string):
    dicionario = {}
    for i in range(len(string)):
        if not string[i] in dicionario:
            dicionario[string[i]] = i
    return dicionario