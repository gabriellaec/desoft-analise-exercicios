def conta_bigramas(s):
    dici={}
    i=0
    while i+2<=len(s):
        a=s[i:i+2]
        if a in dici:
            dici[a]+=1
        else:
            dici[a]=1
        i+=1
    return dici