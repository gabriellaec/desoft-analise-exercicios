def monta_dicionario(x,y):
    dic={}
    for i in x:
        for item in y:
            dic[x[i]]=y[i]
    
    return dic
    