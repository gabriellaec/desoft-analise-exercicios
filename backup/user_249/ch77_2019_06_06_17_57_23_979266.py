def calcula_tempo(dic_atletas):
    dic_atleta_tempo={}
    for k,v in dic_atletas.items():
        dic_atleta_tempo[k]=(200/v)**0,5
    
    return dic_atleta_tempo
    