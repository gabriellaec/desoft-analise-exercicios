def calcula_tempo(dic):
    dic2 = {}
    for k, v in dic.items():
        dic2[k] = (200/v)**(1/2)
    return dic2
