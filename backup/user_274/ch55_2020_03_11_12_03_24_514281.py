def encontra_maximo(l1,l2,l3):
    r1=l1[0]
    r2=l2[0]
    r3=l3[0]
    i=1
    
    while i < 3:
        if l1[i] > r1:
            r1=l1[i]
        if l2[i] > r2:
            r2=l2[i]
        if l3[i] > r3:
            r3=l3[i]
        i=i+1
        
    if r1 >= r2:
        if r1 >= r3:
            return r1
        else:
            return r3
    else:
        if r2 >= r3:
            return r2
        else:
            return r3