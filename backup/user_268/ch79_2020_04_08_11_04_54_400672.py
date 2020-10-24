def monta_dicionario(l1, l2):
    a = len(l1)
    dic = {}
    for i in range(a):
        f = (l1[i])
        b = l2[i]
        c = str(f)
        dic[c] = b
        return dic