def medias_por_inicial(x):
    dicionario = {}
    for nome in x.keys():
        Letra_inicial = x.keys()[0]
        dicionario[Letra_inicial] = x
    return dicionario