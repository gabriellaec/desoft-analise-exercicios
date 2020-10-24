def monta_dicionario(lis1,lis2):
    dic={}
    i=0
    while i<len(lis1):
        dic[i]=i
        i+=1
    return dic
print (monta_dicionario(lis1,lis2))