def calcula_tempo(dic):
    dic2 = {}
    for k, v in dic.items():
        dic2[k] = 10/(v*(1/2))
    return dic2
