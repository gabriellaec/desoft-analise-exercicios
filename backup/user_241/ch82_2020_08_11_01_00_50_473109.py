def primeiras_ocorrencias(string):
    dicionario = {}
    for caractere in string:
        dicionario[caractere] = string.index(caractere)
    return dicionario