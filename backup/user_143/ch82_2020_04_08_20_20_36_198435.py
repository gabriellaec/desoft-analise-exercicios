def primeiras_ocorrencias(s):
    dici={}
    j=0
    k=s[j]
    for i in range(len(s)):
        if s[i]==k:
            x=i
            dici[s[x]]=x
        j+=1
    return dici
            
        