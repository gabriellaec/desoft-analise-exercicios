def calcula_norma(n):
    i=0
    t=0
    s=0
    while i<len(n):
        t=n[i]**2
        s+=t
        i+=1
    v=(s)**0.5
    return v
    
    