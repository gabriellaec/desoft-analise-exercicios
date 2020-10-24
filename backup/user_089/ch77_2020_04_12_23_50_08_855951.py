def calcula_tempo(dic):
    import math
    dic2 = {}
    for e in dic:
        dic2[e] = math.sqrt(200/dic[e])
    return dic2