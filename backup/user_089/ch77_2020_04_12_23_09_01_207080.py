def calcula_tempo(dic):
    import math
    res = {}
    k = dic.keys()
    v = dic.values()
    for e in k:
        if e in v:
            t = math.sqrt(400/v[e])
            res[e] = t
    return res