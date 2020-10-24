def conta_bigramas(string):
    bigramas = []
    i = 0
    while i < (len(string)-1):
        big = string[i] + string[i+1]
        bigramas.append(big)
        i += 1
    dic = {}
    for e in bigramas:
        if e in dic:
            dic[e] += 1
        else:
            dic[e] = 1
    return dic