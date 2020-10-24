def medias_por_inicial(x):
    y={}
    for k,v in x.items():
        y[k[0]]=v
        for m,n in x.items():
            if k[0]==m[0]:
                y[k[0]]=(y[k[0]]+n)/2
        
    return y
        
            