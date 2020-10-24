def quantos_uns(n):
    I=0
    i=0
    n=str(n)
    while i<=len(n):
        if n[i]==1:
            I+=1
        i+=1
    return I
       
    
    