def primeiras_ocorrencias(s):
    dici={}
    i=1
    dici[s[0]]=0
    while i<len(s):
        b=0
        while b<i:
            if s[i]!=s[b]:
                b+=1
            else:
                b=len(s)
        if b==i-1:
            x=i
            dici[s[x]]=x
        i+=1
    return dici
            
        