def acha_bigramas(L):
    i=0
    l=[]
    while i<len(L):
        l.append(L[i:i+2])
        i+=1
    return(l)
        
    