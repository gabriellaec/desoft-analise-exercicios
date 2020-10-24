def medias_por_inicial(n):
    d={}
    t=0
    s=0
    for k,v in n.items():
        if k[0] not in d:
            d[k[0]]=v
            s+=v
            t+=1
        else:
            s+=v
            t+=1
            d[k[0]]=s/t
    return d
       
            
