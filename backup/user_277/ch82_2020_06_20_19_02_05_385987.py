def primeiras_ocorrencias(string):
    dicionario = {}
    for i in range(len(string)):
        if string[i] != string[i-1]:
            dicionario[string[i]] = i
    return dicionario