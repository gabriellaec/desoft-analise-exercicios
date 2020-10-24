def monta_dicionario(lis1,lis2):
    dic = {}
    for i in lis1:
        dic = [i]
        for j in lis2:
            dic[i] = float(j)
    return dic
    
        