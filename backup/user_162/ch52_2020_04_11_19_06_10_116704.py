def calcula_total_da_nota(p, q):
    nf = [0]*len(p)
    i=0
    total = 0
    
    while i < len(p):
        nf[i] = p[i]*q[i]
        i+=1
        
    for i in nf :
        total+=i
        
    return total