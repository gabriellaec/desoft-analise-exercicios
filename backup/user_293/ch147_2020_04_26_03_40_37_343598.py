def mais_frequente(lista):
    dic = {}
    mais_freq = 0
    for e in lista:
        if e not in dic:
            dic[e] = 1
        else:
            dic[e] += 1
        if mais_freq < dic[e]:
            mais_freq = dic[e]
            a = e
    return a