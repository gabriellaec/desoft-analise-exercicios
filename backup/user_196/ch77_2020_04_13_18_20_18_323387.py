def calcula_tempo(dic):
    dicionario = {}
    for nome,aceleracao in dic.items():
        dicionario[nome] = ((200/aceleracao)**(1/2))
    return dicionario