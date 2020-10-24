def conta_bigramas(palavra):
    if len(palavra) < 2:
        return []
    dic = {}
    i = 0
    while i < len(palavra):
        if not i + (i + 1) in dic:
            dic[i + (i + 1)] = 1
        else:
            dic[i + (i + 1)] += 1
    return dic