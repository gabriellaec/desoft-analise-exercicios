def medias_por_inicial(x):
    dicionario = {}
    for nome in x:
        Letra_inicial = x[0]
        dicionario[Letra_inicial] = x
    return dicionario