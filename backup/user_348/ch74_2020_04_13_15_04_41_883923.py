def conta_bigramas(string):
    dicionário = {}
    for bigrama in string:
        if not bigrama in dicionário:
            dicionário[bigrama] = 1
        else:
            dicionário[bigrama] = dicionário[bigrama] + 1
    return dicionário
        