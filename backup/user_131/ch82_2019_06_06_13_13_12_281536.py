def primeiras_ocorrencias(string):
    dicionario = dict()
    for letra in string:
        x = string.find(letra)
        dicionario[letra] = x
    return dicionario
    