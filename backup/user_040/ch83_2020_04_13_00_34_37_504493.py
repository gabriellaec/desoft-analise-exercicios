def medias_por_inicial(x):
    dicionario = {}
    for nome in x.keys():
        Letra_inicial = nome[0]
        dicionario[Letra_inicial] = x.values()
    return dicionario