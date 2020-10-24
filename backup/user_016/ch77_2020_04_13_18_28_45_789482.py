def calcula_tempo(dicionario1):
    dicionario2 = {}
    for i in dicionario1.keys:
        dicionario2[i] = ((200/dicionario1[i])**0.5)
    return dicionario2