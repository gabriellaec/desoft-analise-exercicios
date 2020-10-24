def calcula_tempo (dicionario_atletas):
    dic_tempo={}
    for a in dicionario_atletas:
        dic_tempo[a]=(200/(dicionario_atletas[a]))**(1/2)
    return dic_tempo