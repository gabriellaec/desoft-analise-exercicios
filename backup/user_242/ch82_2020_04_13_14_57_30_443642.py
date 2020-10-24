def primeiras_ocorrencias(string):
    dicionario = {}
    for letra in string:
        dicionario[letra] = string.index(letra)
    return dicionario 