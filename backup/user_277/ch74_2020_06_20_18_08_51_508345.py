def conta_bigramas(string):
    dicionario = {}
    for i in range(len(string)-1):
        bigrama = string[i]+string[i+1]
        if not bigrama in dicionario:
            dicionario[bigrama] = 1
        else:
            dicionario[bigrama] += dicionario[bigrama]
    return dicionario