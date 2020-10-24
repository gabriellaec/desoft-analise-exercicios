dicionario = {}


def primeiras_ocorrencias(string):
    i = 0
    while i < len(string):
        if string[i] not in dicionario:
            dicionario[string[i]] = i
        i += 1
    return dicionario