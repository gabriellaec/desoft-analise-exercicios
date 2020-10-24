def calcula_tempo(dic):
    dic2 = {}
    for e in dic:
        a = dic[e]
        tempo = sqrt(200/a)
        nomedojogador = dic.keys()
        dic2[nomedojogador[e]] = tempo
    return dic2