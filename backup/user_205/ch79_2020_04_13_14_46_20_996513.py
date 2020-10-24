def monta_dicionario(x,y):
    dic={}
    for i in range(len(x)):
        for x in range(len(y)):
            dic[x[i]]=y[x]
    
    return dic
    