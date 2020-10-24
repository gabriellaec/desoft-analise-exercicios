def calcula_tempo(atletas):
    dic={}
    for e,v in atletas.items():
        dic[e]=(200/v)**0.5
    return dic