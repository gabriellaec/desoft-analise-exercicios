def calcula_tempo(dic):
    res = {}
    k = dic.keys()
    v = dic.values()
    for e in k:
        if e in v:
            t = (400/e[v])**(1/2)
            res[e] = t
    return res
    
   
    