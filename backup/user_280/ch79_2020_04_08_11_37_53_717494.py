def monta_dicionario(chaves, valores):
    dicionario = {}
    for i in range(len(chaves)):
        dicionario[chaves[i]] = valores[i]
    return dicionario