def calcula_total_da_nota (p,q):
    total=[]
    for x in zip (p,q):
        total.append(x[0]*x[1])
        
        
    return sum(total)