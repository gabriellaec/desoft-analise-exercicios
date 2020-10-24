def monta_dicionario(l1, l2):
    dic = {}
    i=0
    while i<len(l1):
        dic[l1[i]] = l2[i]
        i+=1
        return dic