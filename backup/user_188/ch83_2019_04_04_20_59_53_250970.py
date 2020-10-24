def medias_por_inicial(dicnotas):
    outdic = {}
    contador = 1
    for nome, nota in dicnotas.items():
        inicial = nome[0]
        if inicial not in outdic:
            outdic[inicial] = nota
        else:
            old = outdic[inicial]
            old *= contador
            contador += 1
            new = (old+nota)/contador
    return outidic 