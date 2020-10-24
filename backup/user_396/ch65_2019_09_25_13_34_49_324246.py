def acha_bigramas(x):
    i = 0
    lis = []
    while i < len(x):
        lis.append(x[i] + x[i+1])
        i +=1
    return lis