def monta_dicionario(l1,l2):
    
    dic = {}
    for e in l1:
        for i in l2:
            dic[l1[e]] = l2[i]
    return dic