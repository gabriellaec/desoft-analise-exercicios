def conta_bigramas(palavra):
    bigramas={}
    i=0
    while i+1<len(palavra):
        big=palavra[i] + palavra[i+1]
        if not big in bigramas:
            bigramas.append(big)
            bigramas[big]=1
        else:
            bigramas[big]+=1
    return bigramas