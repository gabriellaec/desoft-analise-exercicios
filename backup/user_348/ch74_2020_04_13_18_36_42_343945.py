def conta_bigramas(string):
    dicionário = {}
    for i in range(string-1):
        bigrama = string[i] + string[i + 1]
        if not bigrama in dicionário:
            dicionário[bigrama] = 1
        else:
            dicionário[bigrama] = dicionário[bigrama] + 1
    return dicionário
        