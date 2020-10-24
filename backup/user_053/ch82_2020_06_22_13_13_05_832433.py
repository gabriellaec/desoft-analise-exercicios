def primeiras_ocorrencias(string):
    dicionario = {}
    for letra in string:
        if letra not in dicionario.keys():
            dicionario[letra] = string.find(letra)
    return dicionario