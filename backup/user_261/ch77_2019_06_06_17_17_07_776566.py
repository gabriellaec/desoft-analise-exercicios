def calcula_tempo(dicionario):
    d={}
    for nomes,acel in dicionario.items():
        d[nomes]=(200/acel)**0.5
    return d