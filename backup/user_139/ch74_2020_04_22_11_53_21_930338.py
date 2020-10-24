def conta_bigramas(palavra):
    dic = {}
    i = 0
    while i < len(palavra):
        if i + (i + 1) not in dic:
            dic[i + (i + 1)] = 1
        else:
            dic[i + (i + 1)] += 1
    return dic