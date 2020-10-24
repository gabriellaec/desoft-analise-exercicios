def conta_bigramas(s):
    i=0
    dic={}
    while(i<len(s)-1):
        bi=palavra[i]+palvra[i+1]
        if bi in dic:
            dic[bi]+=1
        else:
            dic[bi]=1
        i+=1
    return dic
            