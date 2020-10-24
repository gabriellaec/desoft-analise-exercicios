def monta_dicionario(l1,l2):    
    dic = {}
    for e in range(len(l1)):
        dic[l1[e]] = l2[e]
    return dic