def calcula_tempo(n):
    dicionario2 = {}
    for k, v in n.items():
        dicionario2[k] = ((200/v)**(1/2))
    return dicionario2