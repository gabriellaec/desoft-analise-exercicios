def monta_dicionario(l1, l2):
    a = len(l1)
    dic = {}
    for i in range(a):
        a = str(l1[i])
        b = l2[i]
        dic[a] = b
        return dic