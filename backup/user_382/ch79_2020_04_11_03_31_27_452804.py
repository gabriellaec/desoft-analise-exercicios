def monte_dicionario(l1,l2):
    dic = {}
    for i in l1:
        for t in l2:
            dic[i] = t 
            l2.remove(t)
            break
    return dic 