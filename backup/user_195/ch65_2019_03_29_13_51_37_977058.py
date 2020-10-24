def acha_bigramas(p):
    i=0
    S=[]
    while i<len(p)-1:
        a=p[i:i+2]
        if a in S:
            i+=1
        else:
            S.append(a)
            i+=1
    return S
