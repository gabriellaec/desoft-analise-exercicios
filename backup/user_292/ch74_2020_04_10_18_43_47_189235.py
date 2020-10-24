def conta_bigramas(x):
    d={}
    for i in range(len(x)-1):
        if (x[i]+x[i+1]) not in d:
            d[x[i]+x[i+1]] = 1
        else:
            d[x[i]+x[i+1]] +=1
    return d