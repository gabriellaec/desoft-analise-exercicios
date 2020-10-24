def conta_bigramas(x):
    a = 0
    resp = []
    c1 = 0
    c2 = 2
    while c1 < len(x):
        a = x[c1:c2:]
        resp.append(a)
        c1 += 1
        c2 += 2
    
    aaa = dict()
    b = []
    for i in x:
        b = x.count(i)
        if b > 0:
            aaa[i] = b
            
    return aaa