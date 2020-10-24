def conta_bigramas(palavra):
    dic = {}
    for i in range(len(palavra)-1):
        bigrama = palavra[i]+palavra[i+1]
        if bigrama not in dic:
            dic[bigrama] = 1
        else:
            dic[bigrama] += 1
    return dic