def primeiras_ocorrencias(s):
    dici={}
    i=0
    dici[s[0]]=0
    while i<len(s):
        b=0
        while b<len(s):
            if s[i]!=s[b]:
                x=i
                dici[s[x]]=x
                b=len(s)
            else:
                b+=1
        i+=1
    return dici
            
        