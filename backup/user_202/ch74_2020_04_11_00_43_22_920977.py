def conta_bigramas(t):
    dic = {}
    c = []
    for i in t:
        c.append(i)
    c2 = []
    for i in range(len(c)-1):
        c2.append(c[i]+c[i+1])
    for i in c2:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return(dic)