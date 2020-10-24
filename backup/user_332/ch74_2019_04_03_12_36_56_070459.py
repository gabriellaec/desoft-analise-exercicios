def conta_bigramas(palavra):
    r = len(palavra)-1
    dic = dict()
    for e in range(0,r):
        bi = palavra[e] + palavra[e+1]
        if e in dic:
            dic[bi] += 1
        else:
            dic[bi] = 1
    
    return(dic)