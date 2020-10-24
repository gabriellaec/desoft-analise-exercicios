def medias_por_inicial(dicionario):
    dicionario2 = {}
    for nome in dicionario:
        nota = dicionario[nome]
        letra_inicial = nome[0]
        if not letra_inicial in dicionario2:
            dicionario2[letra_inicial] = nota
        else:
            dicionario[letra_inicial] = (dicionario[letra_inicial] + dicionario[letra_inicial])/2
    return dicionario2