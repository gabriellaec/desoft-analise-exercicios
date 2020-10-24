def conta_bigramas(string):
    dic = dict()
    i = 0
    while i < len(string):
        bigrama = string[i:i+2]
        if bigrama not in dic:
            dic[bigrama] = 1
            i += 1
        else:
            dic[bigrama] += 1
            i += 1
    return dic