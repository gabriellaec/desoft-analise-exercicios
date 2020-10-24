def calcula_tempo(dic):
    dic2 = {}
    for atleta in dic:
        a = dic[atleta]
        tempo = (200/a)**.5
        nomedojogador = dic.values()
        dic2[nomedojogador[atleta]] = tempo
    return dic2