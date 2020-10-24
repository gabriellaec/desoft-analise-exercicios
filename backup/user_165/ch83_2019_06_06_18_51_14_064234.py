def medias_por_inicial(dicionario):
    dicionario_novo = {}
    for nome in dicionario.keys():
        if nome not in dicionario_novo:
            inicial = nome[0]
            dicionario_novo[inicial]
    for notas in dicionario.values():
        for i in range(len(dicionario_novo)):
            dicionario_novo[inicial[i]] = notas[i]
    return dicionario_novo