def conta_letras(string):
    dicionario = {}
    for i in range(len(string)):
        if not string[i] in dicionario:
            dicionario[string[i]] = 1
        else:
            dicionario[string[i]] += 1
    return dicionario