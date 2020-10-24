def monta_dicionario(l1,l2):
    dic = {}
    con = 0
    for i in l1:
        dic[i] = l2[con]
        con +=1
    return dic