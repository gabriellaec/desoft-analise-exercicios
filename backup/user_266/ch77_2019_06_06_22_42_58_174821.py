def calcula_tempo(dic):
    dic2 = dic
    for k, a in dic2.items():
        dic[k] = (100*2/a)**0.5
    return dic2