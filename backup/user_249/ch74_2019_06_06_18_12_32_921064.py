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
        if x not in lis:
            dic[e]=1
        else:
            dic[e]+=1
    
    
    return dic