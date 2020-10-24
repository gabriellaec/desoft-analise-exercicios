def conta_bigramas(txt):
    dic={}
    lis=[]
    i=1
    e=0
    while i<len(txt):
        lis.append(txt[e]+txt[i])
        i+=1
        e+=1
    for x in lis:
        if x not in dic:
            dic[x]=1
        else:
            dic[x]+=1
    
    
    return dic