def conta_bigramas(palavra):
    bigramas={}
    i=0
    o=0
    while i<(len(palavra)-1):
        bi=palavra[i:i+2]
        if bi in bigramas:
            o+=1
        else:
            o=1
        bigramas[bi]=o
        i+=1
    return bigramas 