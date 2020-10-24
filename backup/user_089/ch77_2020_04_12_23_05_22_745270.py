def calcula_tempo(dic):
    res = {}
    k = dic.keys()
    v = dic.values()
    for e in k:
        if e in v:
            t = (400/v[e])**(1/2)
            res[e] = t
    return res
    
   
    