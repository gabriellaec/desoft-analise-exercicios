def conta_bigramas(x):
    dic={}
    i=0
    for e in range(len(x)-1):
        bigrama=x[i]+ x[i+1]
        i+=1
        if bigrama not in dic:
            dic[bigrama]=1
        else:
            dic[bigrama]+=1
            
    return dic
    