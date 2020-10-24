dic_atletas={'atleta1':12,'atleta2':13,'atleta3':11,'atleta4':22,'atleta5':41}
def calcula_tempo(dic_atletas):
    dic_atleta_tempo={}
    for k,v in dic_atletas.items():
        dic_atleta_tempo[k]=(200/v)**0,5
    
    return dic_atleta_tempo
    