def calcula_tempo(dnomes,dtempo):
    nome={}
    tempo={}
    novodic={}
    for nome in dnomes.items() and tempo in dtempo.values():
        novodic=nome[tempo]
    return novodic 