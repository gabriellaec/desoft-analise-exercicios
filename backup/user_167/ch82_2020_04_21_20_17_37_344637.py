def primeiras_ocorrencias (x):
    dic={}
    for e in range(0,len(x)):
        if e  not in dic:
            dic[e]=1
        else:
            dic[e]+=1
     
    return dic    