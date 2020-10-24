def acha_bigrama(p):
    i=0
    bigramas=[]
    while i<len(p)-1:
        c=p[i]+p[i+1]
        if c not in bigramas:
            bigramas.append(p[i]+p[i+1])
        i+=1
    return bigramas