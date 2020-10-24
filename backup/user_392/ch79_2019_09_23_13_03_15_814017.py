def monta_dicionario(x,y):
    dic={}
    i = 0
    while i < len(x):
        dic[x[i]]=y[i]
        i+=1
    return dic
        