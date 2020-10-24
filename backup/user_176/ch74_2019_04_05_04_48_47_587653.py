def conta_bigramas(palavra):
    dic = {}
    for e in range (len(palavra)-1):
        bigrama = palavra[e:e+2]
        dic[bigrama] = 0
    for e in range (len(palavra)-1):
        bigrama = palavra[e:e+2]
        dic[bigrama]+=1
    return dic