def primeiras_ocorrencias(string):
    dicionario = {}
    for i in range(len(string)-1):
        if string[i] not in dicionario:
            dicionario[string[i]] = i
    return dicionario