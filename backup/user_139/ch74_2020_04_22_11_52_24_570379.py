def conta_bigramas(palavra):
    dic = {}
    for e in palavra:
        if e + (e + '1') not in dic:
            dic[e + (e + '1')] = 1
        else:
            dic[e + (e + '1')] += 1
    return dic