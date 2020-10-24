def calcula_tempo(dicionario):
    dic={}
    for atleta, a in dicionario.items():
        t=(200/a)**0.5
        dic[atleta]=t
    return dic