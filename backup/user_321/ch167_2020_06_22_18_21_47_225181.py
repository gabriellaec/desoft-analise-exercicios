def bairro_mais_custoso(dic):
    k = {}
    for i in dic:
        for e in range(6,12):
            if not i in k:
                k[i] = dic[i][e]
            else:
                k[i] += dic[i][e]
    v = 0
    for i in k:
        if k[i] > v:
            v = k[i]
            b = i
    return b