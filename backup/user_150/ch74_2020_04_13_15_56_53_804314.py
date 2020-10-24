def conta_bigramas(string):
    dicionario = {}
    i = 0
    for i in range(len(string)-1):
        bigrama = string[i] + string[i+1]
        if bigrama not in dicionario:
            dicionario[bigrama] = 1
        else:
            dicionario[bigrama] += 1
    return dicionario