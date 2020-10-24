def calcula_tempo (dicionario_atletas):
    dic_tempo={}
    for a in dicionario_atletas:
        dic_tempo[a]=(200/(dicionario_atleta[a]))**(1/2)
    return dic_tempo