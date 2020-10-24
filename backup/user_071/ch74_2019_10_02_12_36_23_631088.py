def conta_bigramas(p):
    i=0
    bigramas=[]
    contagem={}
    while i<len(p)-1:
        c=p[i]+p[i+1]
        bigramas.append(c)
        n=bigramas.count(bigramas[i])
        contagem[bigramas[i]]=n
        i+=1
    return contagem