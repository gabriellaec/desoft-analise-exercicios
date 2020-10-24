def calcula_total_da_nota (p,q):
    total=[]
    i=0
    while i <(len(p)-1):
        total.append(p[i]*q[i])
        i+=1
        
    return total