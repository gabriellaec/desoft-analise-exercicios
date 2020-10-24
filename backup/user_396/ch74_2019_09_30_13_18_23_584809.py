def conta_bigramas(x):
    i = 0
    dic = {}
    while i < len(x)-1:
        bigrama = x[i] + x[i+1]
        if bigrama in dic:
            dic[bigrama] = dic[bigrama]+1
        else:
            dic[bigrama] = 1
        i += 1
    return dic

    