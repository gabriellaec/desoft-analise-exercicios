def conta_bigramas(a):
    dic = {}
    for i in range(len(a)-1):
        dic[a[i]+a[i+1]] += 1 
    return dic
        