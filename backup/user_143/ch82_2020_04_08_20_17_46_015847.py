def primeiras_ocorrencias(s):
    dici={}
    k=s[0]
    for i in range(len(s)):
        if s[i]==k:
            x=i
            dici[s[i]]=i
            
        