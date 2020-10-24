def inverte_dicionario(idades, string):
    dicionario = {}
    for i in range(len(idades)):
        dicionario[idades[i]] = string[i]
    return dicionario