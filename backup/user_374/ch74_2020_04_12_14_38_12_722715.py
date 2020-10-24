def conta_bigramas(oi):
    dic = {}
    for i in range(0,len(oi)):
        b = oi[i:i+2]
        c = len(b)
        
        if c == 2:
            if b not in dic:
                dic[b] = 1
            else:
                dic[b] += 1
    return dic