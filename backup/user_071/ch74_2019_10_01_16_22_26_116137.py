def conta_bigramas(p):
    i=0
    contagem={}
    while i<len(p)-1:
        c=p[i]+p[i+1]
        if c not in contagem:
            contagem[c]=1
        else:
            contagem[c]+=1
            i+=1