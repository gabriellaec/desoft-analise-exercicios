def calcula_tempo(dic):
    dic2 = {}
    for atleta in dic:
        a = dic[atleta]
        tempo = (200/a)**0.5
        nomedojogador = atleta
        dic2[nomedojogador] = tempo
    return dic2