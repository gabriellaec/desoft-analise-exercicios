def bairro_mais_custoso(dicionario):
    dic = {}
    for k in dicionario:
        for v in range(6, 12):
            if not k in dic:
                dic[k] = dicionario[k][v]
            else:
                dic[k] += dicionario[k][v]

    for j in dic:
        vmax = 0
        if dic[j] > vmax:
            vmax = dic[j]
            return j
