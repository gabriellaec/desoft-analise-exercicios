def conta_bigramas(string):
    dic={}
    for e in range(len(string)-1):
        bigrama=string[e:e+2]
        if bigrama not in dic:
            dic[bigrama]=1
        else:
            dic[bigrama]+=1
    return dic
    