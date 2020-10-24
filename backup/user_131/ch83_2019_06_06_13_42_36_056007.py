def medias_por_inicial(dicionario):
    dicionario2 = dict()
    for nome in dicionario:
        if nome[0] not in dicionario2:
            dicionario2[nome[0]] = dicionario[nome]
        else:
            dicionario2[nome[0]] = (dicionario2[nome[0]] + dicionario[nome])/2
    return dicionario2