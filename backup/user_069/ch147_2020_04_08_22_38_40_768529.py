def mais_frequente (lista):
    dic = {}
    for e in lista:
        if not e in dic:
            dic[e] = 1
        else:
            dic[e] += 1
    return max(dic, key=dic.get)
