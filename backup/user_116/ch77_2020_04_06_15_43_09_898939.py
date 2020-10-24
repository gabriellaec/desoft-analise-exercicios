def calcula_tempo(dicat):
    novodic={}
    for nome,ace in dicat.itens():
        novodic[nome]=(100/ace)
    return novodic