def conta_bigramas(s):
    dic = {}
    for i in range(len(s)-1):
        bigrama = string[i] + string[i+1]
        if not bigrama in dic:
            dic[bigrama] = 1
        else:
            dic[bigrama] += 1
    return dic
    