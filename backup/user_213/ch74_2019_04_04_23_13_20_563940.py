def conta_bigramas(palavra):
    bigramas={}
    i=0
    o=0
    while i<(len(palavra)-1):
        bi=palavra[i:i+2]
        if bi in bigramas:
            bigramas[bi]+=1
        else:
            bigramas[bi]=1
        i+=1
    return bigramas 