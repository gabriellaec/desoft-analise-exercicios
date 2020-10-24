def faixa_notas (L1):
    L2 = []
    a = 0
    b = 0
    c = 0
    i = 0
    
    while i < len(L1):
        if L1[i] < 5:
            a += 1
        elif L1[i] >= 5 and L1[i] <= 7:
            b +=1
        else:
            c += 1  
        i += 1
    L2.append(a,b,c)
    return (L2)
        
   