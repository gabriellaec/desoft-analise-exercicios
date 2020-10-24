def calcula_tempo(dicat):
    novodic={}
    for nome,ace in dicat.items():
        novodic[nome]=(100/ace)
    return novodic