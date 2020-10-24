def conta_bigramas(s):
    i=0
    a=dict()
    while(i<len(s)-1):
        bi=palavra[i]+palvra[i+1]
        if bi in a:
            a[bi]+=1
        else:
            a[bi]=1
        i+=1
    return a
            