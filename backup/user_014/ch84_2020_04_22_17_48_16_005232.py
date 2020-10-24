def inverte_dicionario(string, idades):
    dicionario = {}
    for i in range(len(idades)):
        dicionario[idades[i]] = string[i]
    return dicionario