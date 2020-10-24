def monta_dicionario(l1, l2):
    a = len(l1)
    dic = {}
    for i in range(a - 1):
        f = (l1[i])
        b = l2[i]
        dic[f] = b
        return dic