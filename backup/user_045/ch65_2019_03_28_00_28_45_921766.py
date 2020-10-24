def acha_bigramas(n):
    i=0
    t=0
    b=[]
    b[0]=n[i]+n[i+1]
    while i<6:
        b[t]=n[i]+n[i+1]
        i+=1
        t+=1
    return b
        
        
        
    