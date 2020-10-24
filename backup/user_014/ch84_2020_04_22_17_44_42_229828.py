def inverte_dicionario(string, idades):
    dicionario = {}
    for i in range(len(string)):
        dicionario[string[i]] = idades[i]
    return dicionario