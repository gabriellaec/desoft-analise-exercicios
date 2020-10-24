def acha_bigramas(n):
    i=0
    b=[]
    while (i+1)<len(n):
        bigrama=n[i]+n[i+1]
        if bigrama not in b:
            b.append(bigrama)
        i+=1  
    return b
        
        
        
    