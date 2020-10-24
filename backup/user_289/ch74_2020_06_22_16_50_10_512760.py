def conta_bigramas(string):
    dicionario = dict()
    i = 0
    while i < len(string):
        bigrama = string[i:i+1]
        if bigrama not in dicionario.keys:
            dicionario[bigrama] = 1
            i += 1
        else:
            dicionario[bigrama] += 1
            i += 1
    return dicionario
