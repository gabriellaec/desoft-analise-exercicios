def monta_dicionario(lis1,lis2):
    dic={}
    x=0
    for i in lis1:
        dic[i]=lis2[x]
        x+=1
    return dic