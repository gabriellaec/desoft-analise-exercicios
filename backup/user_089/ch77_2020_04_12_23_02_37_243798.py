def calcula_tempo(dic):
    res = {}
    k = dic.keys()
    v = dic.values()
    for e in k:
        if e in v:
            vel = (200*v[e])**(1/2)
            res[e] = vel
    return res
    
   
    