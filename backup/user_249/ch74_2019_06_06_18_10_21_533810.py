txt='casca de ovo'
def conta_bigramas(txt):
    dic={}
    lis=[]
    i=1
    e=0
    while i<len(txt):
        lis.append(txt[e]+txt[i])
        i+=1
        e+=1
    for e in lis:
        if e not in lis:
            dis[e]=1
        else:
            dis[e]+=1
    
    
    return dic