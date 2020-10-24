def monta_dicionario(l1,l2):
    dic={}
    x=len(l1)
    y=len(l2)
    if x==y:
        for i in range (x):
            dic[l1[i]]=l2[i]
    return dic