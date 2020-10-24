def monta_dicionario(x,y):
    dic={}
    for i in range(len(x)):
        for i in range(len(y)):
            dic[x[i]]=y[i]
    
    return dic
    