def calcula_tempo(dic):
    dic2 = {}
    for e in dic:
        a = dic[e]
        tempo = (200/a)**.5
        nomedojogador = dic.keys()
        dic2[nomedojogador[e]] = tempo
    return dic2