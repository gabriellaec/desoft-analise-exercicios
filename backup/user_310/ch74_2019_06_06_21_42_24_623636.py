def conta_bigramas(s):
    d={}
    
    i=0
    
    while i <len(s)-1:
        a= s[i]
        b= s[i+1]
        chave = str(a+b)
        if chave in d:
            d[chave]+=1
        else:
            d[chave] = 1
        i+=1
    
    return d